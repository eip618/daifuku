import discord
from discord.ext import commands
import random
import math

class Memes(commands.Cog):
    """Daifuku meme commands ported from Kurisu."""

    def __init__(self, bot):
        self.bot = bot

    async def _meme(self, ctx, msg, directed: bool = False, image_link: str = None):
        if image_link:
            title = f"{ctx.author.display_name + ':' if not directed else ''} {msg}".strip()
            embed = discord.Embed(title=title if title else discord.Embed.Empty, color=discord.Color.default())
            embed.set_image(url=image_link)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.display_name + ':' if not directed else ''} {msg}".strip())

    @commands.command(hidden=True)
    async def s_99(self, ctx): await self._meme(ctx, "**ALL HAIL BRITANNIA!**")
    @commands.command(hidden=True)
    async def honk(self, ctx): await self._meme(ctx, "`R A K E  I N  T H E  L A K E`")
    @commands.command(hidden=True)
    async def screams(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/screamsinternally.png")
    @commands.command(hidden=True)
    async def eeh(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/eeh.jpg")
    @commands.command(hidden=True)
    async def dubyadud(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/dubyadud.png")
    @commands.command(hidden=True)
    async def inori(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori.gif")
    @commands.command(hidden=True)
    async def inori2(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori2.jpg")
    @commands.command(hidden=True)
    async def inori3(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori3.gif")
    @commands.command(hidden=True)
    async def inori4(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori4.gif")
    @commands.command(hidden=True)
    async def inori5(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori5.png")
    @commands.command(hidden=True)
    async def inori6(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/inori6.gif")
    @commands.command(hidden=True)
    async def shotsfired(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/shotsfired.gif")
    @commands.command(hidden=True)
    async def rusure(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/rusure.gif")
    @commands.command(hidden=True)
    async def r34(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/r34.gif")
    @commands.command(hidden=True)
    async def rip(self, ctx): await self._meme(ctx, "Press F to pay respects.")
    @commands.command(hidden=True)
    async def permabrocked(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/permabrocked.jpg")
    @commands.command(hidden=True)
    async def knp(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/knp.png")
    @commands.command(hidden=True)
    async def lucina(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/lucina.png")
    @commands.command(hidden=True)
    async def lucina2(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/lucina2.jpg")
    @commands.command(hidden=True)
    async def xarec(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/xarec.png")
    @commands.command(hidden=True)
    async def clap(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/clap.gif")
    @commands.command(hidden=True)
    async def ayyy(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/ayyy.png")
    @commands.command(hidden=True)
    async def hazel(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/hazel.png")
    @commands.command(hidden=True)
    async def thumbsup(self, ctx): await self._meme(ctx, "https://nintendohomebrew.com/assets/img/nhmemes/thumbsup.gifv")
    @commands.command(hidden=True)
    async def pbanjo(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/pbanjo.png")
    @commands.command(hidden=True)
    async def whoops(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/2ec4764e884d956fb882f3479fa87ecf.gif")
    @commands.command(hidden=True)
    async def nom(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/nom.png")
    @commands.command(hidden=True)
    async def soghax(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/soghax.png")
    @commands.command(hidden=True)
    async def weebs(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/weebs.png")
    @commands.command(hidden=True)
    async def helpers(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/helpers.png")
    @commands.command(hidden=True)
    async def concern(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/concern.png")
    @commands.command(hidden=True)
    async def fuck(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/fuck.gif")
    @commands.command(hidden=True)
    async def goose(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/goose.jpg")
    @commands.command(hidden=True)
    async def planet(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/planet.png")
    @commands.command(hidden=True)
    async def notreading(self, ctx): await self._meme(ctx, "", image_link="https://nintendohomebrew.com/assets/img/nhmemes/notreading.gif")
    @commands.command(hidden=True)
    async def disgraceful(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/b93b2a99bc28df4a192fc7eb8ccc01a9.png")
    @commands.command(hidden=True)
    async def value(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/f882b32a3f051f474572b018d053bd7b.png")
    @commands.command(hidden=True)
    async def superiority(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/e2cbbf7c808e21fb6c5ab603f6a89a3f.jpg")
    @commands.command(hidden=True)
    async def dolar(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/3ecd851953906ecc2387cfd592ac97e7.png")
    @commands.command(hidden=True)
    async def serotonin(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/2549ac8b197ae68080041d3966a887e8.png")
    @commands.command(hidden=True, aliases=['decisions'])
    async def decision(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/5186160fa1b8002fe8fa1867225e45a7.png")
    @commands.command(hidden=True)
    async def shovels(self, ctx): await self._meme(ctx, "", image_link="https://album.eiphax.tech/uploads/big/b798edd56662f1bde15ae4b6bc9c9fba.png")

    @commands.command(hidden=True)
    async def b(self, ctx):
        b_list = [f"https://nintendohomebrew.com/assets/img/nhmemes/b{i}.png" for i in range(1, 16)]
        await self._meme(ctx, "", image_link=random.choice(b_list))

    # == SHORT VIDEO OR TEXT MEMES ==
    @commands.command(hidden=True)
    async def themoreyouknow(self, ctx): await ctx.send("https://album.eiphax.tech/uploads/big/01432cfa6eb64091301037971f8225c4.webm")
    @commands.command(hidden=True)
    async def cope(self, ctx): await ctx.send("https://album.eiphax.tech/uploads/big/c43dd20db7ff59dec7bc15dd26d2b65f.mp4")
    @commands.command(hidden=True)
    async def didntask(self, ctx): await ctx.send("https://album.eiphax.tech/uploads/big/4f8e77e08460e2234cdaebc6308f1fd1.mp4")

    @commands.command(hidden=True)
    async def doom(self, ctx):
        doom_list = [
            "RIP AND TEAR", "I *could* run Doom, but I choose not to.",
            "The Ion Catapult is designed to use only approved UAC ammunition.",
            "...we will send unto them... only you.",
            "May your thirst for retribution never quench, may the blood on your sword never dry, and may we never need you again.",
            "That is a weapon, NOT a teleporter.",
            "You can't just shoot a hole into the surface of **Mars**...",
            "They are rage, brutal, without mercy. But you. You will be worse. Rip and tear, until it is done."
        ]
        await ctx.send(random.choice(doom_list))

    @commands.command(hidden=True)
    async def hru(self, ctx):
        feeling_list = [
            "AWFUL", "stfu", "alright",
            "I am a bot what the fuck do you think?",
            "Look at the assistance channels for two minutes and tell me how **you** think I am."
        ]
        await ctx.send(random.choice(feeling_list))

    @commands.command(hidden=True)
    async def motd(self, ctx):
        motd_list = [
            "ur mom lol", "hot dogs are sandwiches dont @ me", "have you had a coffee today?",
            "bird app bad", "imagine having opinions in current year", "based", "pog", "ratio",
            "remember to moisturize today!", "drink some water u idiot", "take ur meds",
            "do you like neapolitan ice cream?", "it has been 0 days since eip broke me",
            "The beatings will continue until morale improves.",
            "Hell is empty, and the demons are here.",
            "Man alone measures time. Man alone chimes the hour.",
            "AWFUL", "Alright", "Look at the assistance channels for two minutes and tell me how you think I am."
        ]
        await ctx.send(random.choice(motd_list))

    @commands.command(hidden=True)
    async def warm(self, ctx, u: discord.Member):
        celsius = random.randint(38, 50)
        fahrenheit = math.floor(1.8 * celsius + 32)
        kelvin = math.floor(celsius + 273.15)
        await self._meme(ctx, f"{u.mention} warmed. User is now {celsius}\u00b0C ({fahrenheit}\u00b0F, {kelvin}K).", True)

    @commands.command(hidden=True, aliases=["roast"])
    async def burn(self, ctx, u: discord.Member):
        celsius = random.randint(51, 500)
        fahrenheit = math.floor(1.8 * celsius + 32)
        kelvin = math.floor(celsius + 273.15)
        await self._meme(ctx, f"{u.mention} burned. User is now a crispy {celsius}\u00b0C ({fahrenheit}\u00b0F, {kelvin}K).", True)

    @commands.command(hidden=True, aliases=["cool"])
    async def chill(self, ctx, u: discord.Member):
        celsius = random.randint(-3, 21)
        fahrenheit = math.floor(1.8 * celsius + 32)
        kelvin = math.floor(celsius + 273.15)
        await self._meme(ctx, f"{u.mention} cooled. User is now {celsius}\u00b0C ({fahrenheit}\u00b0F, {kelvin}K).", True)

    @commands.command(hidden=True, aliases=["cryofreeze"])
    async def freeze(self, ctx, u: discord.Member):
        celsius = random.randint(-300, -4)
        fahrenheit = math.floor(1.8 * celsius + 32)
        kelvin = math.floor(celsius + 273.15)
        await self._meme(ctx, f"{u.mention} frozen. User is now {celsius}\u00b0C ({fahrenheit}\u00b0F, {kelvin}K). Wait how is that possible?", True)

    @commands.command(
        hidden=True,
        aliases=["ong", "ongod", "nocap", "ngl", "tbh"],
        help="fr ngl tbh"
    )
    async def fr(self, ctx, sample: int = 1):
        """Returns a selection of zoomerisms for those fr fr moments."""
        sample = max(1, min(sample, 20))
        zoomer_list = [
            "💯", "👌", "🔥", "🙏", "get that bag", "fr",
            "ngl", "tbh", "based", "finna", "tryna", "trynna",
            "flex", "on god", "ong", "bro", "bruh", "real shit",
            "on the real", "deadass", "BFFR", "bestie", "no cap",
            "ratio", "wig", "bussin", "bussin bussin", "fr fr",
            "snatch", "snatched", "ijbol", "we stan", "alr", "slay",
            "lowkey", "💀", "mid", "mf", "goated", "fam",
            "straight up", "🔛 🔝", "🗣️", "‼️", "⁉️", "this goes hard",
            "goes hard", "hard", "tuff", "rigid ngl", "ts", "ts tuff",
            "ts goes hard fr", "and i oop", "sksksk", "bestie", "yasssssss", "squad goals", "gucci fam",
            "fam", "bet", "cap", "no cap", "tea", "spill the tea",
            "iykyk", "jit", "highkey lowkey", "rizz", "W", "L",
            "rizzler", "glow up tbh", "sigma chad", "gyat", "it's giving", "IT'S GIVING FR",
            "gyatt", "fanum tax", "skibidi toilet", "skibidi", "sheesh", "sigma grindset",
            "only in ohio"
        ]
        await ctx.send(' '.join(random.choices(zoomer_list, k=sample)))

async def setup(bot):
    await bot.add_cog(Memes(bot))
