import asyncio
import discord
import datetime
import random
import os
from dotenv import load_dotenv
from discord.ext import commands


intents = discord.Intents().all()
load_dotenv()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('>'), intents=intents)
bot.remove_command('help')
mean_messages = ["how about you ping some bitches instead", "this is harassment", "you want to get sued mate?", "banned"]
footers = ["pain", "aaaaaaa", "why are you doing this", ":(", "hhh", "awa awa", "stop", "192.168.1.15"]
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await load_cogs()
    print("aaa")


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        random_index = random.randrange(len(mean_messages))
        await message.channel.send(mean_messages[random_index])
    await bot.process_commands(message)


@bot.command(name="assign")
@commands.has_permissions(manage_roles=True)
async def assign(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    rolez = int(os.getenv("ROLES"))
    rulez = int(os.getenv("RULES"))
    log_channel = bot.get_channel(int(os.getenv("LOGS")))
    log_embed = discord.Embed(timestamp=ctx.message.created_at, description=
                              f'**{member}** ({member.id}) was let into the server\n \nGod help us all',
                              color=0xfdcf92)
    log_embed.set_author(name=f'{ctx.message.author} ({ctx.message.author.id})', icon_url=member.avatar)
    roleYeet = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleAdd = member.guild.get_role(int(os.getenv("ROLEADD")))
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
                       f"<@{member_id}> now has server access. Don't be a sperg kthx.\nAlso check <#{rulez}> and <#{rolez}>")
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
@assign.error
async def assign_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee fix that shit <@223478168399511562>")  


@bot.command(name="yeet")
@commands.has_permissions(manage_roles=True)
async def yeet(ctx, member: discord.Member):
    user = ctx.message.author.id
    random_feet = random.randrange(len(footers))
    member_id = member.id
    channel = int(os.getenv("DOORMAT"))
    log_channel = bot.get_channel(int(os.getenv("LOGS")))
    log_embed = discord.Embed(timestamp=ctx.message.created_at, description=
                              f'**{member}** ({member.id}) was yoten back to the <#{channel}>\n \nThank fuck',
                              color=0xfdcf92)
    log_embed.set_author(name=f'{ctx.message.author} ({ctx.message.author.id})', icon_url=member.avatar)
    log_embed.set_footer(text=footers[random_feet])
    roleAdd = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleYeet = member.guild.get_role(int(os.getenv("ROLEADD")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    else:
        await member.add_roles(roleAdd)
        await member.remove_roles(roleYeet)
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
        await ctx.send("K.\n"
                       f"{member.mention} was thrown back to <#{channel}>")
@yeet.error
async def assign_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee fix that shit <@223478168399511562>") 


@bot.command(name="guest")
@commands.has_permissions(manage_roles=True)
async def guest(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    rulez = int(os.getenv("RULES"))
    rolez = int(os.getenv("ROLES"))
    log_channel = bot.get_channel(int(os.getenv("LOGS")))
    log_embed = discord.Embed(timestamp=ctx.message.created_at, description=
                              f'**{member}** ({member.id}) was let into the server as a Guest\n \nGod help us all',
                              color=0xfdcf92)
    log_embed.set_author(name=f'{ctx.message.author} ({ctx.message.author.id})', icon_url=member.avatar)
    roleYeet = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleAdd = member.guild.get_role(int(os.getenv("ROLEADD")))
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
                       f"<@{member_id}> now has server access. Don't be a sperg kthx.\nAlso check <#{rulez}> and <#{rolez}>")
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
@assign.error
async def guest_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee fix that shit <@223478168399511562>")  


@bot.command(name='whois', aliases=['who'])
async def whois(ctx, member: discord.Member = None):
    random_feet = random.randrange(len(footers))
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
    embed.set_thumbnail(url = member.avatar)
    embed.add_field(name='User ID:', value=member.id, inline=False)
    embed.add_field(name='Display name:', value=member.display_name)
    embed.add_field(name="Avatar", value=f'[Link]({member.avatar})', inline=False)
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
    embed.set_footer(text=footers[random_feet])
    await ctx.message.reply(embed=embed)


bot.run(os.getenv("TOKEN"))