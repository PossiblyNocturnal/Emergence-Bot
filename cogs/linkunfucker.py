import discord
import aiohttp
from discord.ext import commands

class link_unfucker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
            tweet_links = []
            if "https://x.com" or "https://twitter.com" in message.content:
                 pass
            fxt_embed = discord.Embed(color=discord.Color.blue)
            async with aiohttp.ClientSession() as session:
                for i in tweet_links:
                    async with session.get(i):
                        pass
            # await reply.edit(embed=fxt_embed)


async def setup(bot):
    await bot.add_cog(link_unfucker(bot))
