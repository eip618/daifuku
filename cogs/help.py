from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx):
        """Lists available commands."""
        lines = []
        for command in self.bot.commands:
            if command.hidden or not command.enabled:
                continue
            try:
                can_run = await command.can_run(ctx)
            except commands.CheckFailure:
                can_run = False
            if not can_run:
                continue
            desc = command.help.split("\n")[0] if command.help else "No description."
            lines.append(f"**!{command.name}**: {desc}")
        if lines:
            msg = "**Commands you can use:**\n" + "\n".join(lines)
        else:
            msg = "You don't have access to any commands."
        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Help(bot))
