from discord.ext import commands
from version import __version__

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Checks if the bot is awake."""
        await ctx.send("pong!")

    @commands.command(name='ver', help='Shows the current bot version.')
    async def version(self, ctx):
        """Displays the bot version."""
        await ctx.send(f"I'm currently running **{__version__}**")

async def setup(bot):
    await bot.add_cog(General(bot))
