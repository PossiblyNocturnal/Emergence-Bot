import discord as d
import json
from discord.ext import commands
from datetime import datetime
import aiohttp
import os

class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
async def setup(bot):
    await bot.add_cog(stuff(bot))         