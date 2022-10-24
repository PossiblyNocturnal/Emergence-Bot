import discord
from discord.ext import commands
from datetime import datetime
import aiohttp
import random
from fuzzywuzzy import fuzz


class Warframe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.funne = ["dead game lol", "run while you still can", "unavailable in your region", "play drg instead", "touch grass", 
        "in your balls est. 1984", "this api is weird"]

    @commands.command()
    async def news(self, ctx):
        randfunne = random.randrange(len(self.funne))
        news_embed = discord.Embed(color=0x0081a2, title="Warframe News", timestamp=ctx.message.created_at)
        wflogo = discord.File("images/wf_logo.png", filename="wflogo.png")
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/news") as request:
                news = await request.json()
                for article in reversed(news):
                    url = article["link"]
                    title = article["message"]
                    date = datetime.strptime(article["date"],
                                             '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%#d %B %Y")
                    news_embed.add_field(name=f'{date} | {article["eta"]}', value=f"[{title}]({url})", inline=False)
                    news_embed.set_footer(text=self.funne[randfunne])
                    news_embed.set_thumbnail(url="attachment://wflogo.png")
                await ctx.send(file=wflogo, embed=news_embed)

    @commands.command(name="nw", aliases=["nightwave"])
    async def nightwave(self, ctx):
        randfunne = random.randrange(len(self.funne))
        nwlogo = discord.File("images/nw.webp", filename="nw.webp")
        nw_embed = discord.Embed(color=0x8a0030, title="This week's nightwave", timestamp=ctx.message.created_at)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/nightwave") as request:
                nw = await request.json()
                for challenge in nw["activeChallenges"]:
                    challenge_title = challenge["title"]
                    challenge_desc = challenge["desc"]
                    start = datetime.strptime(challenge["activation"],
                                            '%Y-%m-%dT%H:%M:%S.%fZ')
                    end = datetime.strptime(challenge["expiry"],
                                            '%Y-%m-%dT%H:%M:%S.%fZ')
                    remaining = abs(end.date()-start.date()).days
                    if challenge["reputation"] == 1000:  # Because if challenge["isDaily"] doesn't fucking work
                        nw_embed.add_field(name=f"[Daily] {challenge_title}",
                                           value=f"{challenge_desc}\n**Time remaining**: {remaining} Days", inline=False)
                    if challenge["reputation"] == 4500:
                        nw_embed.add_field(name=f"[Weekly] {challenge_title}",
                                           value=f"{challenge_desc}\n**Time remaining**: {remaining} Days", inline=False)
                    if challenge["isElite"]:
                        nw_embed.add_field(name=f"[Elite Weekly] {challenge_title}",
                                           value=f"{challenge_desc}\n**Time remaining**: {remaining} Days", inline=False)
                nw_embed.set_thumbnail(url="attachment://nw.webp")
                nw_embed.set_footer(text=self.funne[randfunne])
                await ctx.send(file=nwlogo, embed=nw_embed)
        await session.close()

    @commands.command(name="baro")
    async def baro(self, ctx):
        funny = random.randint(1,50)
        randfunne = random.randrange(len(self.funne))
        baro_emblem = discord.File("images/baro.webp", filename="baro.webp")
        if funny == 50:
            baro_embed = discord.Embed(title="Baro Shit'Teer",color=discord.Colour.gold(), timestamp=ctx.message.created_at)
        else:
            baro_embed = discord.Embed(title="Baro Ki'Teer",color=discord.Colour.gold(), timestamp=ctx.message.created_at)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/voidTrader") as request:
                baro = await request.json()
                if not baro["inventory"]:
                    baro_embed.add_field(name="Arrives in", value=baro["startString"], inline=False)
                    baro_embed.add_field(name="Relay:", value=baro["location"], inline=False)
                    baro_embed.add_field(name="Inventory", value="Baro Ki'Teer is yet to arrive.", inline=False)
                else:
                    baro_embed.add_field(name="Relay:", value=baro["location"], inline=False)
                    for item in baro["inventory"]:
                        ducats = item["ducats"]
                        creds = item["credits"]
                        item_name = item["item"]
                        baro_embed.add_field(name=item_name, value=f"{ducats} <:Ducats:573969761109803056> +\n"
                                                                   f"{creds} <:Credits:573969762099527684>")
                baro_embed.set_thumbnail(url="attachment://baro.webp")
                baro_embed.set_footer(text=self.funne[randfunne])
                await ctx.send(file=baro_emblem, embed=baro_embed)
        await session.close()

    @commands.command(name="cetus")
    async def cetus(self, ctx):
        randfunne = random.randrange(len(self.funne))
        ostron = discord.File("images/ostron.webp", filename="ostron.webp")
        cetus_embed = discord.Embed(title="Cetus state", color=discord.Colour.green(),
                                    timestamp=ctx.message.created_at)
        async with aiohttp.ClientSession() as session:
            # Please don't fucking hit me for this implementation I beg you
            async with session.get("https://api.warframestat.us/pc/cetusCycle") as request:
                async with session.get("https://api.warframestat.us/pc/syndicateMissions") as bounties_request:
                    cetus_bounties = await bounties_request.json()
                    cetus_time = await request.json()
                    time_left = cetus_time["shortString"]
                    ostron_syndicate = cetus_bounties[21]
                    if cetus_time["isDay"]:
                        cetus_embed.add_field(name="☀ It's Day!",
                                              value=f"```asciidoc\n= Time Remaining =\n{time_left}\n```", inline=False)
                    else:
                        cetus_embed.add_field(name="🌙 It's Night!",
                                              value=f"```asciidoc\n= Time Left =\n{time_left}\n```", inline=False)
                    cetus_embed.add_field(name="Current Bounties", value="\u200b", inline=False)
                    for jobs in ostron_syndicate["jobs"]:
                        rewards = jobs["rewardPool"]
                        levels = jobs["enemyLevels"]
                        job_name = jobs["type"]
                        rewards_str = ", ".join(rewards)
                        cetus_embed.add_field(name=f"{job_name} | levels {levels[0]} - {levels[1]}",
                                              value=f"```asciidoc\nRewards :: {rewards_str}\n```", inline=False)
                    cetus_embed.set_thumbnail(url="attachment://ostron.webp")
                    cetus_embed.set_footer(text=self.funne[randfunne])
                    await ctx.send(file=ostron, embed=cetus_embed)
        await session.close()

    @commands.command(name="vallis")
    async def vallis(self, ctx):
        randfunne = random.randrange(len(self.funne))
        su_emblem = discord.File("images/solaris.webp", filename="solaris.webp")
        vallis_embed = discord.Embed(title="Orb Vallis state", color=discord.Colour.blue(),
                                     timestamp=ctx.message.created_at)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/vallisCycle") as request:
                async with session.get("https://api.warframestat.us/pc/syndicateMissions") as bounties_request:
                    vallis_time = await request.json()
                    vallis_bounties = await bounties_request.json()
                    vallis_syndicate = vallis_bounties[23]
                    time_left = vallis_time["shortString"]
                    if vallis_time["isWarm"]:
                        vallis_embed.add_field(name="🔥 It's Warm! 🔥",
                                               value=f"```asciidoc\n= Time Remaining =\n{time_left}\n```", inline=False)
                    else:
                        vallis_embed.add_field(name="❄ It's Cold! ❄",
                                               value=f"```asciidoc\n= Time Remaining =\n{time_left}\n```", inline=False)
                    vallis_embed.add_field(name="Current Bounties", value="\u200b")
                    for jobs in vallis_syndicate["jobs"]:
                        rewards = jobs["rewardPool"]
                        levels = jobs["enemyLevels"]
                        job_name = jobs["type"]
                        rewards_str = ", ".join(rewards)
                        vallis_embed.add_field(name=f"{job_name} | levels {levels[0]} - {levels[1]}",
                                               value=f"```asciidoc\nRewards :: {rewards_str}\n```", inline=False)
                    vallis_embed.set_thumbnail(url="attachment://solaris.webp")
                    vallis_embed.set_footer(text=self.funne[randfunne])
                    await ctx.send(file=su_emblem, embed=vallis_embed)
        await session.close()

    @commands.command(name="cambion")
    async def cambion(self, ctx):
        emblem = discord.File("images/entrati.webp", filename="entrati.webp")
        randfunne = random.randrange(len(self.funne))
        cambion_embed = discord.Embed(title="Cambion Drift bounties", color=discord.Colour.orange(),
                                      timestamp=ctx.message.created_at)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/cambionCycle") as request:
                async with session.get("https://api.warframestat.us/pc/syndicateMissions") as bounties_request:
                    cambion_bounties = await bounties_request.json()
                    cambion_syndicate = cambion_bounties[21]
                    cycle = await request.json()
                    if cycle["active"] == "vome":
                        cambion_embed.add_field(name='🔹Vome🔹', value=f'```asciidoc\n= Time Remaining =\n{cycle["timeLeft"]}```', inline=False)
                    else:
                        cambion_embed.add_field(name='🔺Fass🔻', value=f'```asciidoc\n= Time Remaining =\n{cycle["timeLeft"]}```', inline=False)
                    for jobs in cambion_syndicate["jobs"]:
                        rewards = jobs["rewardPool"]
                        levels = jobs["enemyLevels"]
                        job_name = jobs["type"]
                        rewards_str = ", ".join(rewards)
                        cambion_embed.add_field(name=f"{job_name} | levels {levels[0]} - {levels[1]}",
                                                value=f"```asciidoc\nRewards :: {rewards_str}\n```", inline=False)
                    cambion_embed.set_thumbnail(url="attachment://entrati.webp")
                    cambion_embed.set_footer(text=self.funne[randfunne])
                    await ctx.send(file=emblem, embed=cambion_embed)
        await session.close()

    @commands.command(name="sortie")
    async def sorties(self, ctx):
        randfunne = random.randrange(len(self.funne))
        emblem = discord.File("images/sortie.png", filename="sortie.png")
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/sortie") as request:
                sortie = await request.json()
                faction = sortie["faction"]
                mission_no = 0
                sortie_embed = discord.Embed(title=f"Today's Sortie | {faction}", color=discord.Colour.purple(),
                                             timestamp=ctx.message.created_at)
                sortie_embed.add_field(name="Time left", value=sortie["eta"], inline=False)
                for mission in sortie["variants"]:
                    modifier = mission["modifier"]
                    modifier_desc = mission["modifierDescription"]
                    node = mission["node"]
                    mission_type = mission["missionType"]
                    sortie_embed.add_field(name=f"Mission #{mission_no + 1} | {node}",
                                           value=f"**Mission type:** {mission_type}"
                                                 f"\n**Modifier:** {modifier}"
                                                 f"\n**Description:** {modifier_desc}", inline=False)
                    mission_no += 1
                sortie_embed.set_thumbnail(url="attachment://sortie.png")
                sortie_embed.set_footer(text=self.funne[randfunne])
                await ctx.send(file=emblem, embed=sortie_embed)
        await session.close()

    @commands.command(name="riven", aliases=["riv"])
    async def riven(self, ctx, *, name):
        randfunne = random.randrange(len(self.funne))
        emblem = discord.File("images/Samodeus.webp", filename="samo.webp")
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.warframestat.us/pc/rivens") as request:
                rivens = await request.json()
                for query in rivens:
                    for wep in rivens[query]:
                        if fuzz.token_sort_ratio(name.split()[:2], wep.split()[:2]) == 100: # Only compare first 2 words so people don't have to type "Veiled Archgun Riven Mod" and could just type "Veiled Archgun"
                            wepinfo = rivens[query][wep]
                            if "veiled" in name.lower(): # Veiled rivens don't have rerolled info so no need to parse unrolled info
                                embed = discord.Embed(title=f'Riven info for: {wepinfo["unrolled"]["compatibility"]}', color=0xa45ee5, 
                                timestamp=ctx.message.created_at)
                                embed.add_field(name=wepinfo["unrolled"]["compatibility"], 
                                value=f'Average value: {round(wepinfo["unrolled"]["avg"])} <:Platinum:573969761919303720>'
                                f'\nMin Price: {wepinfo["unrolled"]["min"]} <:Platinum:573969761919303720>'
                                f'\nMax Price: {wepinfo["unrolled"]["max"]} <:Platinum:573969761919303720>'
                                f'\nMedian Price: {wepinfo["unrolled"]["median"]} <:Platinum:573969761919303720>', inline=False)
                                embed.add_field(name="⚠️All info comes from Trade Chat via Warframe's API. \nBot does not take warframe.market and riven.market into account.", value='\u200b')
                            else:
                                embed = discord.Embed(title=f'Riven info for: {wepinfo["unrolled"]["compatibility"]}', color=0xa45ee5, 
                                timestamp=ctx.message.created_at)
                                if not "veiled" in name.lower():
                                    embed.add_field(name="More info about this Riven:", value=f"[Click Me]({'https://semlar.com/rivenprices/'+name.lower()})")
                                embed.add_field(name='Unrolled', 
                                value=f'Average value: {round(wepinfo["unrolled"]["avg"])} <:Platinum:573969761919303720>'
                                f'\nMin Price: {wepinfo["unrolled"]["min"]} <:Platinum:573969761919303720>'
                                f'\nMax Price: {wepinfo["unrolled"]["max"]} <:Platinum:573969761919303720>'
                                f'\nMedian Price: {wepinfo["unrolled"]["median"]} <:Platinum:573969761919303720>', inline=False)

                                embed.add_field(name=f'Rerolled', 
                                value=f'Average value: {round(wepinfo["rerolled"]["avg"])} <:Platinum:573969761919303720>'
                                f'\nMin Price: {wepinfo["rerolled"]["min"]} <:Platinum:573969761919303720>'
                                f'\nMax Price: {wepinfo["rerolled"]["max"]} <:Platinum:573969761919303720>'
                                f'\nMedian Price: {wepinfo["rerolled"]["median"]} <:Platinum:573969761919303720>', inline=False)
                                embed.add_field(name="⚠️All info comes from Trade Chat via Warframe's own API. \nBot does not take warframe.market and riven.market into account.", value='\u200b')

                            embed.set_thumbnail(url="attachment://samo.webp")
                            embed.set_footer(text=self.funne[randfunne])
                            await ctx.send(file=emblem, embed=embed)
        await session.close()


async def setup(bot):
    await bot.add_cog(Warframe(bot))
