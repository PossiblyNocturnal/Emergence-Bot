import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import argparse
import random

parser = argparse.ArgumentParser(
    prog="Emergence",
    description="A simple multipurpose Discord bot for whatever feat. Warframe commands",
)
parser.add_argument(
    "-t",
    "--test",
    action="store_true",
    help="uses test bot's token instead of the production one",
)
args = parser.parse_args()
if args.test:
    prefix = "^"
else:
    prefix = ">"

intents = discord.Intents().all()
load_dotenv()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

mean_messages = [
    "how about you ping some bitches instead",
    "this is harassment",
    "you want to get sued mate?",
    "banned",
    "keep yourself safe:)",
    "why are you doing this",
    "My head... turning into metal... folds in my brain, being flattened...",
    "hey you should probably play Limbus Company",
    "https://media.discordapp.net/attachments/548944483165929477/1185095740339523696/attachment-2-1.gif?ex=65cef6ea&is=65bc81ea&hm=172b3d13d3096ddc36668e705e5e98af59edcfc2d24dba21687e26a35e1b2c18&"
]


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"k logged in as {bot.user}")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        random_index = random.randrange(len(mean_messages))
        await message.channel.send(mean_messages[random_index])
    await bot.process_commands(message)
    
@bot.tree.command(name="ping", description="what do you think it does lol")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency: {round(bot.latency * 1000)} ms")
    
@bot.command(name="undoormat")
@commands.has_permissions(manage_roles=True)
async def assign(ctx, member: discord.Member):
    user = ctx.message.author.id
    member_id = member.id
    role_yeet = member.guild.get_role(int(os.getenv("HADIYEET")))
    role_add = member.guild.get_role(int(os.getenv("HADIADD")))
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
        await ctx.message.add_reaction("✅")


@assign.error
async def assign_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have perms to do that you dumbfuck")
    else:
        print(error)
        await ctx.message.add_reaction("❌")
        await ctx.send("Shit brokey again go fix it <@223478168399511562>")

if args.test:
    try:
        print("k using test bot's token(or trying, at least)")
        bot.run(os.getenv("TEST_TOKEN"))
    except:
        print("You fucked something up retard go fix it")
else:
    try:
        print("Using main bot's token now.")
        bot.run(os.getenv("HADITOKEN"))
    except:
        print("this also doesnt work lol")