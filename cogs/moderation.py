from discord.ext import commands
import discord

PROBATION_ROLE_NAME = "Probation"

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- DB Functions ---

    async def get_warn_count(self, guild_id, user_id):
        async with self.bot.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "SELECT count FROM warns WHERE guild_id=%s AND user_id=%s",
                    (guild_id, user_id)
                )
                row = await cur.fetchone()
                return row[0] if row else 0

    async def set_warn_count(self, guild_id, user_id, count):
        async with self.bot.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO warns (guild_id, user_id, count) VALUES (%s, %s, %s) "
                    "ON DUPLICATE KEY UPDATE count=%s",
                    (guild_id, user_id, count, count)
                )

    async def log_punishment_role(self, guild_id, user_id, role_id):
        async with self.bot.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO punishment_roles (guild_id, user_id, role_id) VALUES (%s, %s, %s) "
                    "ON DUPLICATE KEY UPDATE added_at=NOW()",
                    (guild_id, user_id, role_id)
                )

    async def remove_punishment_role_log(self, guild_id, user_id, role_id):
        async with self.bot.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "DELETE FROM punishment_roles WHERE guild_id=%s AND user_id=%s AND role_id=%s",
                    (guild_id, user_id, role_id)
                )

    async def get_punishment_roles(self, guild_id, user_id):
        async with self.bot.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "SELECT role_id FROM punishment_roles WHERE guild_id=%s AND user_id=%s",
                    (guild_id, user_id)
                )
                return [row[0] for row in await cur.fetchall()]

    # --- Role helpers ---

    def get_probation_role(self, guild: discord.Guild):
        return discord.utils.get(guild.roles, name=PROBATION_ROLE_NAME)

    # --- Command Handlers ---

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} (reason: {reason})')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} (reason: {reason})')

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, minutes: int, *, reason=None):
        until = discord.utils.utcnow() + discord.timedelta(minutes=minutes)
        await member.timeout(until, reason=reason)
        await ctx.send(f'{member.mention} timed out for {minutes} minutes. Reason: {reason}')

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        guild_id = ctx.guild.id
        user_id = member.id
        current = await self.get_warn_count(guild_id, user_id)
        new_count = current + 1
        await self.set_warn_count(guild_id, user_id, new_count)
        await ctx.send(f'{member.mention} warned ({new_count}/5). Reason: {reason}')
        if new_count == 3:
            await ctx.send(f'{member.mention} has 3 warns and will be kicked.')
            try:
                await member.kick(reason="Auto-kick: 3 warns")
            except Exception as e:
                await ctx.send(f"Failed to kick: {e}")
        elif new_count == 5:
            await ctx.send(f'{member.mention} has 5 warns and will be banned.')
            try:
                await member.ban(reason="Auto-ban: 5 warns")
            except Exception as e:
                await ctx.send(f"Failed to ban: {e}")

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warns(self, ctx, member: discord.Member):
        guild_id = ctx.guild.id
        user_id = member.id
        count = await self.get_warn_count(guild_id, user_id)
        await ctx.send(f'{member.mention} has {count} warn(s).')

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def clearwarns(self, ctx, member: discord.Member):
        guild_id = ctx.guild.id
        user_id = member.id
        await self.set_warn_count(guild_id, user_id, 0)
        await ctx.send(f"{member.mention}'s warns cleared.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def probate(self, ctx, member: discord.Member):
        probation_role = self.get_probation_role(ctx.guild)
        if not probation_role:
            await ctx.send(f"Role '{PROBATION_ROLE_NAME}' not found.")
            return
        if probation_role in member.roles:
            await ctx.send(f"{member.mention} is already on probation.")
            return
        await member.add_roles(probation_role, reason="Placed on probation")
        await self.log_punishment_role(ctx.guild.id, member.id, probation_role.id)
        await ctx.send(f"{member.mention} is now on probation.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unprobate(self, ctx, member: discord.Member):
        probation_role = self.get_probation_role(ctx.guild)
        if not probation_role:
            await ctx.send(f"Role '{PROBATION_ROLE_NAME}' not found.")
            return
        if probation_role not in member.roles:
            await ctx.send(f"{member.mention} is not on probation.")
            return
        await member.remove_roles(probation_role, reason="Probation lifted")
        await self.remove_punishment_role_log(ctx.guild.id, member.id, probation_role.id)
        await ctx.send(f"{member.mention} is no longer on probation.")

    @commands.command(name="applyrole", aliases=["punish"])
    @commands.has_permissions(manage_roles=True)
    async def applyrole(self, ctx, member: discord.Member, *, role_name: str):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            await ctx.send(f"Role `{role_name}` not found.")
            return
        if role in member.roles:
            await ctx.send(f"{member.mention} already has the `{role_name}` role.")
            return
        try:
            await member.add_roles(role, reason=f"Role applied via {ctx.command} by {ctx.author}")
            await self.log_punishment_role(guild.id, member.id, role.id)
            await ctx.send(f"{member.mention} has been given the `{role_name}` role.")
        except discord.Forbidden:
            await ctx.send(f"I do not have permission to assign the `{role_name}` role.")
        except Exception as e:
            await ctx.send(f"Failed to assign role: `{e}`")

    @commands.command(name="removerole", aliases=["unpunish"])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, *, role_name: str):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            await ctx.send(f"Role `{role_name}` not found.")
            return
        if role not in member.roles:
            await ctx.send(f"{member.mention} does not have the `{role_name}` role.")
            return
        try:
            await member.remove_roles(role, reason=f"Role removed via {ctx.command} by {ctx.author}")
            await self.remove_punishment_role_log(guild.id, member.id, role.id)
            await ctx.send(f"{role_name} role has been removed from {member.mention}.")
        except discord.Forbidden:
            await ctx.send(f"I do not have permission to remove the `{role_name}` role.")
        except Exception as e:
            await ctx.send(f"Failed to remove role: `{e}`")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Reapplies punishment roles if a punished user rejoins."""
        role_ids = await self.get_punishment_roles(member.guild.id, member.id)
        for role_id in role_ids:
            role = member.guild.get_role(role_id)
            if role and role not in member.roles:
                try:
                    await member.add_roles(role, reason="Restored punishment role after rejoin")
                except Exception as e:
                    print(f"Failed to reapply role {role_id} to {member}: {e}")

    @commands.command(
        name="purge",
        aliases=["clean", "clear"],
        help="Delete a number of messages, or messages by user/content. Usage: .purge [count=100] [@user] [string]"
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, count: int = 100, member: discord.Member = None, *, search: str = None):
        """Delete messages in the current channel. See help for usage."""
        # remove invoking message
        try:
            await ctx.message.delete()
        except Exception:
            pass  # pass if no perms

        def predicate(msg):
            if member and msg.author != member:
                return False
            if search and search.lower() not in msg.content.lower():
                return False
            return True

        deleted = []
        async for msg in ctx.channel.history(limit=min(count, 1000), oldest_first=False):
            if msg.id == ctx.message.id:
                continue  # safer, probably unnecessary
            if predicate(msg):
                deleted.append(msg)
            if len(deleted) >= count:
                break

        if not deleted:
            conf = await ctx.send("No messages found to delete with those parameters.")
            await conf.delete(delay=5)
            return

        try:
            await ctx.channel.delete_messages(deleted)
        except Exception:
            for msg in deleted:
                try:
                    await msg.delete()
                except Exception:
                    pass

        confirmation = await ctx.send(f"🧹 Deleted {len(deleted)} message(s).")
        await confirmation.delete(delay=5)

    @purge.error
    async def purge_error(self, ctx, error):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        if isinstance(error, commands.MissingPermissions):
            conf = await ctx.send("You need the 'Manage Messages' permission to use this command.")
            await conf.delete(delay=5)
        elif isinstance(error, commands.BadArgument):
            conf = await ctx.send("Invalid arguments. Usage: `.purge [count=100] [@user] [string]`")
            await conf.delete(delay=5)
        else:
            conf = await ctx.send("An error occurred while processing the command.")
            await conf.delete(delay=5)


async def setup(bot):
    await bot.add_cog(Moderation(bot))
