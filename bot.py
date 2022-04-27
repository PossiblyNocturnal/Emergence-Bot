import discord
import datetime
import random
import os
import json
from dotenv import load_dotenv
from discord.ext import commands


intents = discord.Intents().all()
load_dotenv()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('>'), intents=intents)
bot.remove_command('help')
mean_messages = ["how about you ping some bitches instead", "this is harassment", "you want to get sued mate?"]

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("aaa")
    

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        random_index = random.randrange(len(mean_messages))
        await message.channel.send(mean_messages[random_index])
    await bot.process_commands(message)


@bot.command(name="assign")
@commands.has_any_role(904539351805988865, 732646084744183899)
async def assign(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    channel = bot.get_channel(904535607383048192)
    log_channel = bot.get_channel(959022627811385395)
    log_embed = discord.Embed(timestamp=ctx.message.created_at, description=
                              f'**{member}** ({member.id}) was let into the server\n \nGod help us all',
                              color=0xfdcf92)
    log_embed.set_author(name=f'{ctx.message.author} ({ctx.message.author.id})', icon_url=member.avatar_url)
    roleYeet = member.guild.get_role(959023639062261770)
    roleAdd = member.guild.get_role(959576398475984927)
    
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    elif roleAdd in member.roles:
        await ctx.message.add_reaction("❌")
        await ctx.send("user already has access to the server you ape")
    else:
        await member.remove_roles(roleYeet)
        await member.add_roles(roleAdd)
        await ctx.send(f'K.\n' 
                       f"<@{member_id}> now has server access. Don't be a sperg kthx")
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
@assign.error
async def assign_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee")  


@bot.command(name="yeet")
@commands.has_any_role(732646084744183899)
async def yeet(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    channel = bot.get_channel(904535607383048192)
    log_channel = bot.get_channel(959022627811385395)
    log_embed = discord.Embed(timestamp=ctx.message.created_at, description=
                              f'**{member}** ({member.id}) was yoten back to the <#904535607383048192>\n \nThank fuck',
                              color=0xfdcf92)
    log_embed.set_author(name=f'{ctx.message.author} ({ctx.message.author.id})', icon_url=member.avatar_url)
    log_embed.set_footer(text="pain")
#    roleYeet = member.guild.get_role(959576398475984927)
    roleAdd = member.guild.get_role(959023639062261770)
    
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    # elif roleAdd in member.roles:
    #     await ctx.message.add_reaction("❌")
    #     await ctx.send("no")
    else:
        roles = [role.id for role in member.roles]
        for role in roles[1:]:
            r = member.guild.get_role(role)  
            await member.remove_roles(r)
        await member.add_roles(roleAdd)
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
        await ctx.send("K.\n"
                       f"{member.mention} was thrown back to the <#904535607383048192>")
@yeet.error
async def assign_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee")  



@bot.command(name='whois', aliases=['who'])
async def whois(ctx, member: discord.Member = None):
    if not member: # Shows message author's info when no target is specified.
        member = ctx.message.author  

    # ━━━Fetches current time and date, as well as date when a user created an account and joined the server.━━
    now = datetime.datetime.now().date()
    date2 = member.joined_at.date()
    date3 = member.created_at.date()
    # ━━━━Counts days since server join and account registration━━━━
    c_diff = abs(now - date3).days
    j_diff = abs(now - date2).days
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    roles = [role.mention for role in member.roles[1:]]
    embed = discord.Embed(color=0xffa07a, title=f'User info of {member}', timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='User ID:', value=member.id, inline=False)
    embed.add_field(name='Display name:', value=member.display_name)
    embed.add_field(name="Avatar", value=f'[Link]({member.avatar_url})', inline=False)
    embed.add_field(name='Joined at:',
                    value=member.joined_at.strftime(f"%a, %#d %B %Y, %I:%M %p UTC ({j_diff} days ago)"),
                    inline=False)
    embed.add_field(name='Account created at:', value=member.created_at.strftime(
        f"%a, %#d %B %Y, %I:%M %p UTC ({c_diff} days ago)"),
                    inline=False)
    embed.add_field(name="Roles:", value='   '.join(roles), inline=False)
    embed.add_field(name="Top role:", value=member.top_role.mention, inline=False)
    embed.add_field(name="Current status:", value=f'{member.status}', inline=True)
    if member.activity == None:
        embed.add_field(name="Current Activity:", value=member.activity,
                        inline=True)  # Prevents NoneType error thingy(tm) when user has no activity set.
    else:
        embed.add_field(name="Current Activity:", value=member.activity.name, inline=True)
    if member.bot:
        embed.add_field(name='Bot/Human:', value='Bot', inline=True)
    else:
        embed.add_field(name='Bot/Human:', value='Human', inline=True)
    embed.set_footer(text='please help me')
    await ctx.message.reply(embed=embed)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
    

bot.run(os.getenv("TOKEN"))