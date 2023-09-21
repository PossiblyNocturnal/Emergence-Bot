import discord
import datetime
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
import re
import asyncio
import argparse


parser = argparse.ArgumentParser(
    prog="NotRay",
    description="A simple multipurpose Discord bot for whatever feat. Warframe commands",
)
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
intents = discord.Intents().all()
load_dotenv()
bot = commands.Bot(command_prefix=">", intents=intents)
bot.remove_command("help")
mean_messages = [
    "how about you ping some bitches instead",
    "this is harassment",
    "you want to get sued mate?",
    "banned",
    "keep yourself safe:)",
]
footers = [
    "pain",
    "aaaaaaa",
    "why are you doing this",
    ":(",
    "hhh",
    "awa awa",
    "stop",
    "192.168.0.1 get doxxed loser",
    "you should play va11 hall-a tbh",
]


@bot.event
async def on_ready():
    await bot.tree.sync()
    await load_cogs()
    print(f"k logged in as {bot.user}")


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        random_index = random.randrange(len(mean_messages))
        await message.channel.send(mean_messages[random_index])
    elif message.channel.id == 1114616834591838258 and message.author.id != bot.user.id:
        taco_check = re.search(r"🌮", message.content.strip())
        taco_plead_check = re.search(r":taco_plead:", message.content.strip())
        if taco_check or taco_plead_check:
            pass
        else:
            retard_role = discord.utils.get(
                message.guild.roles,
                name="tacoless and bitchless",  # I know using role name instead of id is retarded cry harder
            )
            await message.author.add_roles(retard_role)
            await message.delete()
            await message.channel.send(
                f"<@{message.author.id}> retard you broke the 🌮 chain", delete_after=5
            )
            await asyncio.sleep(300)
            await message.author.remove_roles(retard_role)
    elif (
        message.author.id == 320241358440759307
        or message.author.id == 694913462760898580
    ):
        if message.author.id == 320241358440759307:
            await message.add_reaction("🌮")
        else:
            await message.add_reaction("🐴")
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
        value="`news\nnightwave\nbaro\ncetus\nvallis\ncambion\nsortie\nriven\n`",
    )
    em.add_field(name="Misc", value="`whois\n8ball`")
    em.set_footer(text=footers[random_feet], icon_url=bot.user.avatar.url)

    await ctx.send(embed=em)


@help.command(aliases=["who"])
async def whois(ctx):
    em = discord.Embed(
        title=">whois",
        description="Provides basic info about a user. If no argument is provided, shows info about you.\n **DOES NOT "
        "SHOW INFO ABOUT USERS NOT ON THE SERVER**",
        color=0xDB9A7E,
    )
    em.add_field(name="**Aliases**", value="who")
    em.add_field(
        name="**Usage**", value=">whois `@member`\n >whois `member_id`\n >whois"
    )
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
    await ctx.send(embed=em)


@help.command(aliases=["8ball"])
async def _8ball(ctx):
    em = discord.Embed(
        title=">8ball",
        description="Do I really need to tell you what 8ball does? Come on",
        color=0xDB9A7E,
    )
    em.add_field(name="**Aliases**", value="8ball")
    em.add_field(name="**Usage**", value=">8ball your question")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
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
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
    await ctx.send(embed=em)


@help.command(aliases=["riv"])
async def riven(ctx):
    em = discord.Embed(
        title=">riven",
        description="Shows info about Trade Chat Riven Prices according to Warframe's own riven API.",
        color=0x00DFFF,
    )
    em.add_field(name="**Aliases**", value="riven\n riv")
    em.add_field(name="**Usage**", value=">riven `Weapon Name`")
    random_feet = random.randrange(len(footers))
    em.set_footer(text=footers[random_feet], icon_url=ctx.guild.icon.url)
    await ctx.send(embed=em)


@bot.command(aliases=["8ball"])  # Literally just a  boring 8ball command.
async def _8ball(ctx):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    await ctx.message.reply(f"Answer: {random.choice(responses)}")


@bot.command(name="assign")
@commands.has_permissions(manage_roles=True)
async def assign(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    # rolez = int(os.getenv("ROLES"))
    # rulez = int(os.getenv("RULES"))
    log_channel = bot.get_channel(int(os.getenv("LOGS")))
    log_embed = discord.Embed(
        timestamp=ctx.message.created_at,
        description=f"**{member}** ({member.id}) was let into the server\n \nGod help us all",
        color=0xFDCF92,
    )
    log_embed.set_author(
        name=f"{ctx.message.author} ({ctx.message.author.id})", icon_url=member.avatar
    )
    role_yeet = member.guild.get_role(int(os.getenv("ROLEYEET")))
    role_add = member.guild.get_role(int(os.getenv("ROLEADD")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    elif role_add in member.roles:
        await ctx.message.add_reaction("❌")
        await ctx.send("user already has access to the server you ape")
    else:
        await member.remove_roles(role_yeet)
        await member.add_roles(role_add)
        await ctx.send(
            f"K.\n" f"<@{member_id}> now has server access. Don't be a sperg kthx."
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
    role_add = member.guild.get_role(int(os.getenv("ROLEYEET")))
    if member_id == user:
        await ctx.message.add_reaction("❌")
        await ctx.send("retard you can't use it on yourself")
    else:
        for role in member.roles[1:]:
            await member.remove_roles(role)
            await member.add_roles(role_add)
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
        name="Server join date:",
        value=member.joined_at.strftime(
            f"%a, %#d %B %Y, %I:%M %p UTC ({j_diff} days ago)"
        ),
        inline=False,
    )
    embed.add_field(
        name="Account creation date:",
        value=member.created_at.strftime(
            f"%a, %#d %B %Y, %I:%M %p UTC ({c_diff} days ago)"
        ),
        inline=False,
    )
    embed.add_field(name="Roles:", value="   ".join(roles), inline=False)
    embed.add_field(name="Top role:", value=member.top_role.mention, inline=False)
    embed.add_field(name="Current status:", value=f"{member.status}", inline=True)
    if member.activity is None:
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
    embed.set_footer(text=footers[random_feet], icon_url=bot.user.avatar.url)
    await ctx.message.reply(embed=embed)


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


if args.test:
    try:
        print("k using test bot's token(or trying, at least)")
        bot.run(os.getenv("TEST_TOKEN"))
    except:
        print("You fucked something up retard go fix it")
else:
    try:
        print("Using main bot's token now.")
        bot.run(os.getenv("TOKEN"))
    except:
        print("this also doesnt work lol")
