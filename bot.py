import discord
import datetime
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands


intents = discord.Intents().all()
load_dotenv()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(">"), intents=intents)
bot.remove_command("help")
mean_messages = [
    "how about you ping some bitches instead",
    "this is harassment",
    "you want to get sued mate?",
    "banned",
]
footers = [
    "pain",
    "aaaaaaa",
    "why are you doing this",
    ":(",
    "hhh",
    "awa awa",
    "stop",
    "192.168.1.15, get doxxed",
]


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.wait_until_ready()
    await load_cogs()
    print("aaa")


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        random_index = random.randrange(len(mean_messages))
        await message.channel.send(mean_messages[random_index])
    await bot.process_commands(message)


@bot.tree.command(name="ping", description="what do you think lol")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency: {round(bot.latency * 1000)} ms")


@bot.group(invoke_without_command=True)
async def help(ctx):
    random_feet = random.randrange(len(footers))
    em = discord.Embed(
        title="Available Commands",
        description="Use >help `command` to get more info",
        color=0xDB9A7E,
    )
    em.add_field(
        name="Warframe stuff",
        value="news\n nightwave\n baro\n cetus\n vallis\n cambion\n sortie\n riven\n",
    )
    em.add_field(name="Misc", value="whois")
    em.set_footer(text=footers[random_feet])

    await ctx.send(embed=em)


@help.command(aliases=["who"])
async def whois(ctx):
    em = discord.Embed(
        title=">whois",
        description="Provides basic info about a user. If no argument is provided, shows info about you.\n **DOES NOT SHOW INFO ABOUT USERS NOT ON THE SERVER**",
        color=0xDB9A7E,
    )
    em.add_field(name="**Aliases**", value="who")
    em.add_field(
        name="**Usage**", value=">whois `@member`\n >whois `member_id`\n >whois"
    )
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def news(ctx):
    em = discord.Embed(
        title=">news", description="Shows recent News from Warframe.", color=0x00DFFF
    )
    em.add_field(name="**Aliases**", value="news")
    em.add_field(name="**Usage**", value=">news")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command(aliases=["nw"])
async def nightwave(ctx):
    em = discord.Embed(
        title=">nightwave",
        description="Shows current Nightwave Challenges.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="nw\n nightwave")
    em.add_field(name="**Usage**", value=">nightwave")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def baro(ctx):
    em = discord.Embed(
        title=">baro",
        description="If Baro is present, shows his stock and location. Otherwise shows ETA.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="baro")
    em.add_field(name="**Usage**", value=">baro")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def vallis(ctx):
    em = discord.Embed(
        title=">vallis",
        description="Shows Orb Vallis bounties and Time of Day.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="vallis")
    em.add_field(name="**Usage**", value=">vallis")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def cetus(ctx):
    em = discord.Embed(
        title=">cetus",
        description="Shows Cetus bounties and Time of Day.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="cetus")
    em.add_field(name="**Usage**", value=">cetus")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def cambion(ctx):
    em = discord.Embed(
        title=">cambion",
        description="Shows Cambion Drift bounties and Current Cycle.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="cambion")
    em.add_field(name="**Usage**", value=">cambion")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command()
async def sortie(ctx):
    em = discord.Embed(
        title=">sortie",
        description="Shows current Sortie Missions and Modifiers.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="sortie")
    em.add_field(name="**Usage**", value="sortie")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@help.command(aliases=["riv"])
async def riven(ctx):
    em = discord.Embed(
        title=">riven",
        description="Shows info about Trade Chat Riven Prices",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="riven\n riv")
    em.add_field(name="**Usage**", value=">riven `Weapon Name`")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet])
    await ctx.send(embed=em)


@bot.command(name="assign")
@commands.has_permissions(manage_roles=True)
async def assign(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    rolez = int(os.getenv("ROLES"))
    rulez = int(os.getenv("RULES"))
    log_channel = bot.get_channel(int(os.getenv("LOGS")))
    log_embed = discord.Embed(
        timestamp=ctx.message.created_at,
        description=f"**{member}** ({member.id}) was let into the server\n \nGod help us all",
        color=0xFDCF92,
    )
    log_embed.set_author(
        name=f"{ctx.message.author} ({ctx.message.author.id})", icon_url=member.avatar
    )
    roleYeet = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleAdd = member.guild.get_role(int(os.getenv("ROLEADD")))
    guest = member.guild.get_role(int(os.getenv("GUEST")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    elif roleAdd in member.roles:
        await ctx.message.add_reaction("❌")
        await ctx.send("user already has access to the server you ape")
    else:
        await member.remove_roles(roleYeet, guest)
        await member.add_roles(roleAdd)
        await ctx.send(
            f"K.\n"
            f"<@{member_id}> now has server access. Don't be a sperg kthx.\nAlso check <#{rulez}> and <#{rolez}>"
        )
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
    log_embed = discord.Embed(
        timestamp=ctx.message.created_at,
        description=f"**{member}** ({member.id}) was yoten back to the <#{channel}>\n \nThank fuck",
        color=0xFDCF92,
    )
    log_embed.set_author(
        name=f"{ctx.message.author} ({ctx.message.author.id})", icon_url=member.avatar
    )
    log_embed.set_footer(text=footers[random_feet])
    roleAdd = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleYeet = member.guild.get_role(int(os.getenv("ROLEADD")))
    guest = member.guild.get_role(int(os.getenv("GUEST")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    else:
        await member.add_roles(roleAdd)
        await member.remove_roles(roleYeet, guest)
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")
        await ctx.send("K.\n" f"{member.mention} was thrown back to <#{channel}>")


@yeet.error
async def yeet_error(ctx, error):
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
    roleYeet = member.guild.get_role(int(os.getenv("ROLEYEET")))
    roleAdd = member.guild.get_role(int(os.getenv("GUEST")))
    mem = member.guild.get_role(int(os.getenv("ROLEADD")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    elif roleAdd in member.roles:
        await ctx.message.add_reaction("❌")
        await ctx.send("user already has access to the server you ape")
    elif mem in member.roles:
        await member.remove_roles(mem)
        await member.add_roles(roleAdd)
        log_embed = discord.Embed(
            timestamp=ctx.message.created_at,
            description=f"**{member}** ({member.id}) is now just a Guest\n \nlmao",
            color=0xFDCF92,
        )
        log_embed.set_author(
            name=f"{ctx.message.author} ({ctx.message.author.id})",
            icon_url=member.avatar,
        )
        await ctx.message.add_reaction("✅")
        await ctx.send(f"K <@{member_id}> is a Guest now")
        await log_channel.send(embed=log_embed)
    else:
        await member.remove_roles(roleYeet)
        await member.add_roles(roleAdd)
        log_embed = discord.Embed(
            timestamp=ctx.message.created_at,
            description=f"**{member}** ({member.id}) was let into the server as a Guest\n \nGod help us all",
            color=0xFDCF92,
        )
        log_embed.set_author(
            name=f"{ctx.message.author} ({ctx.message.author.id})",
            icon_url=member.avatar,
        )
        await ctx.send(
            f"K.\n"
            f"<@{member_id}> now has server access. Don't be a sperg kthx.\nAlso check <#{rulez}> and <#{rolez}>"
        )
        await log_channel.send(embed=log_embed)
        await ctx.message.add_reaction("✅")


@guest.error
async def guest_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("eee fix that shit <@223478168399511562>")


@bot.command(name="whois", aliases=["who"])
async def whois(ctx, member: discord.Member = None):
    random_feet = random.randrange(len(footers))
    if not member:  # Shows message author's info when no target is specified.
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
    embed = discord.Embed(
        color=0xFFA07A, title=f"User info of {member}", timestamp=ctx.message.created_at
    )
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="User ID:", value=member.id, inline=False)
    embed.add_field(name="Display name:", value=member.display_name)
    embed.add_field(name="Avatar", value=f"[Link]({member.avatar})", inline=False)
    embed.add_field(
        name="Joined at:",
        value=member.joined_at.strftime(
            f"%a, %#d %B %Y, %I:%M %p UTC ({j_diff} days ago)"
        ),
        inline=False,
    )
    embed.add_field(
        name="Account created at:",
        value=member.created_at.strftime(
            f"%a, %#d %B %Y, %I:%M %p UTC ({c_diff} days ago)"
        ),
        inline=False,
    )
    embed.add_field(name="Roles:", value="   ".join(roles), inline=False)
    embed.add_field(name="Top role:", value=member.top_role.mention, inline=False)
    embed.add_field(name="Current status:", value=f"{member.status}", inline=True)
    if member.activity == None:
        embed.add_field(
            name="Current Activity:", value=member.activity, inline=True
        )  # Prevents NoneType error thingy(tm) when user has no activity set.
    else:
        embed.add_field(
            name="Current Activity:", value=member.activity.name, inline=True
        )
    if member.bot:
        embed.add_field(name="Bot/Human:", value="Bot", inline=True)
    else:
        embed.add_field(name="Bot/Human:", value="Human", inline=True)
    embed.set_footer(text=footers[random_feet])
    await ctx.message.reply(embed=embed)


bot.run(os.getenv("TOKEN"))
