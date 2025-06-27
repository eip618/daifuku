from discord.ext import commands
import os
import subprocess

class CogControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reloadall(self, ctx):
        cogs = [f[:-3] for f in os.listdir("./cogs") if f.endswith(".py")]
        loaded, failed = 0, []
        for cog in cogs:
            cogname = f"cogs.{cog}"
            try:
                if cogname in self.bot.extensions:
                    await self.bot.reload_extension(cogname)
                else:
                    await self.bot.load_extension(cogname)
                loaded += 1
            except Exception as e:
                failed.append(f"`{cog}`: {e}")
        msg = f"♻️ Reloaded {loaded} cogs."
        if failed:
            msg += "\nFailed:\n" + "\n".join(failed)
        await ctx.send(msg)

    @commands.command(name="quit")
    @commands.has_permissions(administrator=True)
    async def quit(self, ctx):
        await ctx.send("♻️ Restarting Daifuku...")
        try:
            subprocess.Popen(["sudo", "systemctl", "restart", "daifuku"])
        except Exception as e:
            await ctx.send(f"Failed to restart: `{e}`")
        os._exit(0)

async def setup(bot):
    await bot.add_cog(CogControl(bot))
