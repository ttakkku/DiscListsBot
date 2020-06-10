import discord 

from discord.ext import commands, tasks 
from discord.utils import get 

from urllib.request import Request 
import urllib 
import bs4

import json 

client = commands.Bot(command_prefix = "-")
client.remove_command('list')
client.remove_command('help')

@client.event 
async def on_ready():
    status_time.start()

@client.event 
async def on_member_join(member):

    role = get(member.guild.roles, id=697762004940619787)
    await member.add_roles(role)
    await member.edit(nick="[ 1학년 ] " + str(member.name))

@tasks.loop(seconds=5)
async def status_time():
    guild = client.get_guild(695877575255261306)
    await client.change_presence(activity=discord.Game("Document: " + str(len(set(guild.get_channel(718828639944310865).text_channels))) + ", Channels: " + str(len(set(guild.text_channels)))))

@client.command()
async def invites(ctx):

    guild = client.get_guild(ctx.channel.guild.id)
    invites = await guild.invites()
    embed = discord.Embed(title="DISCLISTS INVITES", color=discord.Colour.from_rgb(47, 49, 54))

    for invite in invites:
        embed.add_field(name=invite.code, value=str(invite.created_at) + ": " + str(invite.uses), inline=False)

    await ctx.send(embed=embed)

@client.command()
async def do(ctx, name):

    guild = client.get_guild(695877575255261306)

    name = name.replace(" ", "-")

    for channels in guild.text_channels:
        if str(channels.name) == str(name):
            await ctx.send("이미 중복된 채널이 있습니다")
            return 

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(send_messages=False),
        ctx.author: discord.PermissionOverwrite(send_messages=True)
    }

    channel = await guild.get_channel(718828639944310865).create_text_channel(name=name, topic="해당 채널은 <@" + str(ctx.author.id) + ">님의 문서입니다", overwrites=overwrites)
    msg = await guild.get_channel(channel.id).send("<@" + str(ctx.author.id) + ">")

    await msg.delete()
    await ctx.message.add_reaction('🚀')

@client.command()
async def dos(ctx, name):

    try: 

        name = name.replace(" ", "-")

        guild = client.get_guild(695877575255261306)

        for channels in guild.get_channel(718828639944310865).text_channels:
            if str(channels.name) == str(name):
                embed = discord.Embed(title=f"DOCUMENT NAME: {channels.name}", color=discord.Colour.from_rgb(47, 49, 54))
                embed.add_field(name="문서 생성자:", value=channels.topic, inline=False)
                embed.add_field(name="문서 생성 날짜:", value=channels.created_at, inline=False)
                await ctx.send(embed=embed)
                return 

        await ctx.send("해당 문서를 찾을 수 없습니다!")

    except AttributeError as error: 
        await ctx.send("`" + str(error) + "`")
    except EnvironmentError as error:
        await ctx.send("`" + str(error) + "`")
    except EOFError as error:
        await ctx.send("`" + str(error) + "`")
    except: 
        await ctx.send("정확한 에러를 찾을 수 없습니다!")

@client.command()
async def email(ctx, email, content):
    
    guild = client.get_guild(695877575255261306)

    email = email.replace(" ", "-")

    for channel in guild.get_channel(719539332792451143).text_channels:
        if str(channel.name) == str(email):

            if int(channel.topic) == int(ctx.author.id):
                await ctx.send("본인 이메일에 보낼 수 없습니다!")
                return 
            else: 
                embed = discord.Embed(color=discord.Colour.from_rgb(47, 49, 54))
                embed.add_field(name=str(ctx.author) + "님이 전송한 내용 입니다:", value=content)
                await client.get_channel(channel.id).send(embed=embed, content=f"<@{channel.topic}>")
                await ctx.message.add_reaction('💌')
                return 

    await ctx.send("해당 이메일을 찾을 수 없습니다")

@client.command()
async def email_create(ctx, email):

    email = email.replace(" ", "-")

    guild = client.get_guild(695877575255261306)

    for channel in guild.get_channel(719539332792451143).text_channels:

        if str(channel.name) == str(email):
            await ctx.send("중복되는 이메일이 있습니다")
            return 

        if int(channel.topic) == int(ctx.author.id):
            await ctx.send("이미 보유하고 있는 이메일이 있습니다")
            return 

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(send_messages=False, read_messages=True)
    }

    channel = await guild.get_channel(719539332792451143).create_text_channel(name=email, topic=ctx.author.id, overwrites=overwrites)
    msg = await guild.get_channel(channel.id).send("<@" + str(ctx.author.id) + ">")

    await msg.delete()
    await ctx.message.add_reaction('🚀')

@client.command()
async def pas(ctx, o):

    if o == "off":
        role = get(ctx.author.roles, id=719859191908401182)
        if not role in ctx.author.roles:
            await ctx.send("이미 비공개 채널로 설정된 상태입니다")
        else:
            await ctx.send("성공적으로 비공개로 설정하였습니다")

            roles = get(ctx.author.guild.roles, id=719859191908401182)
            member = ctx.author
            await member.remove_roles(roles)

    if o == "on":
        role = get(ctx.author.roles, id=719859191908401182)
        if role in ctx.author.roles:
            await ctx.send("이미 공개 채널로 설정된 상태입니다")
        else:
            await ctx.send("성공적으로 공개로 설정하였습니다")

            roles = get(ctx.author.guild.roles, id=719859191908401182)
            member = ctx.author 
            await member.add_roles(roles)

    if not o == "on" and not o == "off":
        await ctx.send("해당 메뉴를 찾을 수 없습니다!")

@client.command()
async def github(ctx, name, github=None):

    try: 

        if github == None: 
   
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://api.github.com/users/' + str(name) + "?xml=1"
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            obj = bs4.BeautifulSoup(html, "html.parser")
  
            with open('./github/github.json', 'w', encoding="UTF-8") as w:
                w.write(str(obj))
                w.close()

            with open('./github/github.json', 'r', encoding="UTF-8") as r:
                gi = json.load(r)
                gi_id = gi["id"]
                gi_type = gi["type"]
                gi_company = gi["company"]
                gi_name = gi["name"]
                gi_location = gi["location"]
                gi_email = gi["email"]
                gi_public_repos = gi["public_repos"]
                gi_followers = gi["followers"]
                gi_following = gi["following"]
                gi_created_at = gi["created_at"]
                gi_updated_at = gi["updated_at"]
                r.close()

            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://api.github.com/users/' + str(name) + "?xml=1"
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            obj = bs4.BeautifulSoup(html, "html.parser")

            if gi_company == None:
                gi_company = "회사를 찾을 수 없습니다"
            if gi_location == None:
                gi_location = "위치를 찾을 수 없습니다"
            if gi_email == None:
                gi_email = "이메일을 찾을 수 없습니다"

            embed = discord.Embed(title="GITHUB", color=discord.Colour.from_rgb(47, 49, 54))
            embed.add_field(name="깃허브 닉네임:", value=gi_name, inline=False)
            embed.add_field(name="깃허브 아이디:", value=gi_id, inline=False)
            embed.add_field(name="깃허브 타입:", value=gi_type, inline=False)
            embed.add_field(name="깃허브 프로필: 회사", value=gi_company, inline=False)
            embed.add_field(name="깃허브 프로필: 위치", value=gi_location, inline=False)
            embed.add_field(name="깃허브 프로필: 이메일", value=gi_email, inline=False)
            embed.add_field(name="깃허브 프로필: 공개 레포지토리", value=gi_public_repos, inline=False)
            embed.add_field(name="깃허브 프로필: 내 팔로우", value=gi_followers, inline=False)
            embed.add_field(name="깃허브 프로필: 팔로잉", value=gi_following, inline=False)
            embed.add_field(name="깃허브 프로필: 계정 생성 날짜", value=gi_created_at, inline=False)
            embed.add_field(name="깃허브 프로필: 업데이트 날짜", value=gi_updated_at, inline=False)
            await ctx.send(embed=embed)

        if github == "orgs":

            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://api.github.com/users/' + str(name) + "/orgs"
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            obj = bs4.BeautifulSoup(html, "html.parser")

            with open('./github/github.json', 'w', encoding="UTF-8") as w:
                w.write(str(obj))
                w.close()

            with open('./github/github.json', 'r', encoding="UTF-8") as r:
                gi = json.load(r)
                embed = discord.Embed(title="GITHUB ORGS", color=discord.Colour.from_rgb(47, 49, 54))

                github_group = 0
                for gis in gi:

                    github_group += 1
                    embed.add_field(name=gis["login"], value="https://github.com/" + str(gis["login"]), inline=False)

            r.close()
            await ctx.send(embed=embed)

    except:

        await ctx.send("해당 정보를 찾을 수 없습니다!")

    
@client.command()
async def help(ctx):

    embed = discord.Embed(color=discord.Colour.from_rgb(47, 49, 54))
    embed.add_field(name="-email_create <email-name>", value="내 이메일을 새로 생성합니다", inline=False)
    embed.add_field(name='-email <email-name> "content"', value="그 이메일에 내용을 전송합니다", inline=False) 
    embed.add_field(name="-invites", value="현재 사용하고 있는 초대 에셋을 불러옵니다", inline=False)
    embed.add_field(name="-do <document-name>", value="해당 문서를 생성합니다", inline=False)
    embed.add_field(name="-dos <document-name>", value="해당 문서를 찾아 정보를 조회 합니다", inline=False)
    embed.add_field(name="-pas <on/off>", value="파트너 채널을 공개 채널로 전환합니다 (사용자)", inline=False)
    embed.add_field(name="-github <name> <detailed=None>", value="깃허브에서 프로필 정보를 조회 합니다", inline=False)
    embed.set_footer(text="해당 봇은 파이썬 기반으로 제작되었습니다: DISCLISTS TEAM")
    await ctx.send(embed=embed)

client.run('coken')
