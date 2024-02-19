import discord
import aiohttp
from discord.ext import commands

class link_unfucker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
            pass
            # await reply.edit(embed=fxt_embed)


async def setup(bot):
    await bot.add_cog(link_unfucker(bot))
