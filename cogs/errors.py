from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        err_channel = discord.utils.get(ctx.guild.text_channels, name='bot-err')
        dest = err_channel or ctx.channel

        if isinstance(error, commands.MissingRequiredArgument):
            msg = f"Missing argument: `{error.param.name}`."
        elif isinstance(error, commands.BadArgument):
            msg = "One or more arguments were invalid."
        elif isinstance(error, commands.MissingPermissions):
            msg = "You don’t have permission to use that command."
        elif isinstance(error, commands.BotMissingPermissions):
            msg = "I don’t have the required permissions."
        elif isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            msg = f"That command is on cooldown. Try again in {round(error.retry_after, 2)}s."
        else:
            msg = f"An error occurred: `{type(error).__name__}: {error}`"
        try:
            await dest.send(msg)
        except Exception:
            pass

async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
