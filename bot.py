import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os
import aiomysql

load_dotenv()

TOKEN = os.getenv("DAIFUKU_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = ["!", "."], intents=intents, help_command=None)

async def create_db_pool():
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    db = os.getenv("MYSQL_DB")
    return await aiomysql.create_pool(
        host=host,
        user=user,
        password=password,
        db=db,
        autocommit=True
    )

async def create_tables(db_pool):
    async with db_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                CREATE TABLE IF NOT EXISTS warns (
                    guild_id BIGINT NOT NULL,
                    user_id BIGINT NOT NULL,
                    count INT DEFAULT 0,
                    PRIMARY KEY (guild_id, user_id)
                )
            """)
            await cur.execute("""
                CREATE TABLE IF NOT EXISTS punishment_roles (
                    guild_id BIGINT NOT NULL,
                    user_id BIGINT NOT NULL,
                    role_id BIGINT NOT NULL,
                    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (guild_id, user_id, role_id)
                )
            """)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name='mods')
        if channel:
            try:
                await channel.send("🤖 Daifuku is online and ready for moderation duty!")
            except Exception as e:
                print(f"Failed to send startup message to {guild.name}: {e}")

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

async def main():
    # 1. Set up shared DB pool and attach to bot
    bot.db_pool = await create_db_pool()
    # 2. Ensure tables exist
    await create_tables(bot.db_pool)
    # 3. Load all cogs (now safe to access bot.db_pool)
    await load_cogs()
    # 4. Start the bot
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
