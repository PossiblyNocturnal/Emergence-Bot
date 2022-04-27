import discord as d
import json
from discord.ext import commands
from datetime import datetime
import aiohttp
import os

class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def vc(self, ctx, name = None):
        uid_str = str(ctx.message.author.id)
        if not name:
            name = f"{ctx.message.author.name}'s VC"
        if os.stat("vc.json").st_size == 0: # If the file is empty, creates vc and writes info into the file
            vcj = open("vc.json", "r+")
            ch = await ctx.guild.create_voice_channel(name=name, category=self.bot.get_channel(959609148507562004))
            c_info = {uid_str: {"Channel_name":ch.name, "Channel_id":ch.id}}
            json.dump(c_info, vcj)
            await ctx.send("Created **{}**".format(ch.name))
        elif os.stat("vc.json").st_size != 0:
            vcj = open("vc.json", "r")
            vcd = json.load(vcj)
            if uid_str in vcd and vcd[uid_str]["Channel_id"] == "NaN": #If user had a vc but deleted it, create vc and updates entry
                ch = await ctx.guild.create_voice_channel(name=name, category=self.bot.get_channel(959609148507562004))
                c_info = {uid_str: {"Channel_name":ch.name, "Channel_id":ch.id}}
                with open("vc.json", "w") as vcjw:
                    json.dump(c_info, vcjw)
                await ctx.send("Created **{}**".format(ch.name))
            elif uid_str not in vcd:
                ch = await ctx.guild.create_voice_channel(name=name, category=self.bot.get_channel(959609148507562004))
                c_info = {uid_str: {"Channel_name":ch.name, "Channel_id":ch.id}}
                with open("vc.json", "r+") as vcjw:
                    vd = json.load(vcjw)
                    vd.update(c_info)
                    json.dump(vd, vcjw)
                await ctx.send("Created **{}**".format(ch.name))
            else:
                await ctx.send("Deleting **{}**...".format(vcd[uid_str]["Channel_name"]))
                await self.bot.get_channel(vcd[uid_str]["Channel_id"]).delete()
                vcd[uid_str]["Channel_id"] = "NaN"
                with open("vc.json", "w") as vcjw:
                    json.dump(vcd, vcjw)
        else:
            await ctx.send("h")
            
                
    
    
    #@commands.command()
    #async def aaa(self, ctx, cat1, cat2):
    #    embed = discord.Embed(color=discord.Colour.blurple(), title="bruh")
    #    async with aiohttp.ClientSession() as session:
    #        async with session.get("https://api.waifu.pics/"+cat1+cat2) as request:
    #            j = await request.json()
    #            embed.set_image(url=j["url"])
    #            
    #    await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(stuff(bot))
            