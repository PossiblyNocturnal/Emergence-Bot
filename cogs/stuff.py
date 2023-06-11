import discord
import asyncio
from discord.ext import commands

# TODO   Add per-server config for role add/yeet and don't kill yourself
class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                   
                           
async def setup(bot):
    await bot.add_cog(stuff(bot))         