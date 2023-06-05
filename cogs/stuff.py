import discord
from discord.ext import commands

class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # TODO   Add per-server config for role add/yeet and don't kill yourself
    # @commands.command()
    # @commands.is_owner()
    # async def init(self, ctx):
    #     with open("servers.json") as prefs:
    #         dic_t = json.load(prefs)
    #     if ctx.guild.id in dic_t.keys():
    #         await ctx.send("no I'm good")
    #     else:
    #         template = {
    #                 ctx.guild.id : {
    #                     "role_to_yeet" : "",
    #                     "role_to_add" : "",
    #                     "remove_all_roles_on_yeet" : ""
    #                         }
    #                     }
    #         dic_t.update(template)
    #         with open("servers.json", "w") as prefs:
    #             json.dump(dic_t, prefs)
    #         await ctx.send("aight added this server to the list")
                
        
        
async def setup(bot):
    await bot.add_cog(stuff(bot))         