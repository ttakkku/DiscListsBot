import discord 

from random import randrange 
from discord.ext import commands

from urllib.request import Request 
import urllib 
import bs4

client = commands.Bot(command_prefix = "v")
client.remove_command('help')

@client.event 
async def on_ready():
    if client.is_ready:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="VALORANTE MUSIC"), status=discord.Status.idle)

@client.command()
async def 도움말(ctx):
    
    embed = discord.Embed(title="WELCOME TO VALORANTE BOT!", color=discord.Colour.from_rgb(47, 49, 54))
    embed.add_field(name="v통계 [이름] (미완성)", value="요청한 사용자의 통계를 표시합니다", inline=False)
    embed.add_field(name="v무기 [무기 이름]", value="요청된 무기에 대한 정보를 불러옵니다", inline=False)
    embed.add_field(name="v에이전트 [에이전트 이름]", value="요청한 에이전트에 대한 정보를 불러옵니다", inline=False)
    embed.add_field(name="v맵 [맵 이름]", value="요청한 맵에 대한 정보를 불러옵니다", inline=False)
    embed.add_field(name="v패치", value="발로란트 패치 내용을 불러옵니다", inline=False)
    embed.set_footer(text='보다 더 자세한 명령어를 확인하고 싶다면 "v확인 (명령어)"를 입력해주세요!')
    await ctx.send(embed=embed)

@client.command()
async def 확인(ctx, commands):
    if commands == "무기":
        embed = discord.Embed(color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="현재 존재하는 무기:", value="- 스팅어\n- 스펙터\n- 버키\n- 저지\n- 불독\n- 가디언\n- 밴달\n- 팬텀\n- 마샬\n- 오퍼레이터\n- 아레스\n- 오딘\n- 클래식\n- 쇼티\n- 프렌지\n- 고스트\n- 셰리프")
        embed.set_image(url="https://cdn.discordapp.com/attachments/717356740777345119/719779943046840330/356b6baec9850cad.png")
        await ctx.send(embed=embed)
    if commands == "에이전트":
        embed = discord.Embed(color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="현재 존재하는 에이전트:", value="- 브림스톤\n- 세이지\n- 소바\n- 제트\n- 피닉스\n- 레이즈\n- 바이퍼\n- 브리치\n- 사이퍼\n- 오멘\n- 레이나")
        embed.set_image(url="https://cdn.discordapp.com/attachments/717356740777345119/717356883089948692/49305b4857c3dc32.png")
        await ctx.send(embed=embed)

    if commands == "맵":
        embed = discord.Embed(color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="현재 존재하는 맵:", value="- 헤이븐\n- 바인드\n- 스플릿")
        await ctx.send(embed=embed)


@client.command()
async def 통계(ctx, name=None):
    await ctx.send("준비중인 기능입니다")

@client.command()
async def 무기(ctx, name):

    if name == "스팅어":
        embed = discord.Embed(title="Stinger", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="20")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 18발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.15배율) 4점사, 탄퍼짐 감소\n- 연사 속도: 초당 4발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "스펙터":
        embed = discord.Embed(title="Specter", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="30")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 13.33발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.15배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 12발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "버키":
        embed = discord.Embed(title="Bucky", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="5")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 1.1발", inline=False)
        embed.add_field(name="보조 공격", value="- 반자동 공중 파열(주 공격보다 먼 거리)\n- 연사 속도: 초당 1.1발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "저지":
        embed = discord.Embed(title="Jerzi", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="7")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 18발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "불독":
        embed = discord.Embed(title="Bulldog", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="24")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 9.15발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.25배율) 3점사\n- 연사 속도: 초당 4발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "가디언":
        embed = discord.Embed(title="Guardian", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="12")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 6.5발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.5배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 6.5발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "밴달":
        embed = discord.Embed(title="Bandal", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="25")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 9.25발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.25배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 8.32발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "팬텀":
        embed = discord.Embed(title="Phantom", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="30")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 11발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.15배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 9.9발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "마샬":
        embed = discord.Embed(title="marshall", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="5")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 1.5발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (2.5배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 1.2발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "오퍼레이터":
        embed = discord.Embed(title="Operator", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="5")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 0.75발", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 이중 확대 (2.5배율, 5배율), 탄퍼짐 대폭 감소\n- 연사 속도: 초당 0.75발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "아레스":
        embed = discord.Embed(title="Ares", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="50")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 10 -> 13발 (연사 시 증가)", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.25배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 13 -> 13발 (연사 시 증가)", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "오딘":
        embed = discord.Embed(title="Odin", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="100")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 12 -> 15.6발 (연사 시 증가)", inline=False)
        embed.add_field(name="보조 공격", value="- 조준경 확대 (1.25배율), 탄퍼짐 약간 감소\n- 연사 속도: 초당 15.6발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "클래식":
        embed = discord.Embed(title="Classic", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="12")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 6.75발", inline=False)
        embed.add_field(name="보조 공격", value="- 3점사, 탄퍼짐 증가\n- 연사 속도: 초당 2.22발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "쇼티":
        embed = discord.Embed(title="Shorty", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="2")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 3.3발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "프렌지":
        embed = discord.Embed(title="Fringe", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="13")
        embed.add_field(name="주 공격", value="- 완전 자동 사격\n- 연사 속도: 초당 10발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "고스트":
        embed = discord.Embed(title="Ghost", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="15")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 6.75발", inline=False)
        await ctx.send(embed=embed)
        return 
    if name == "셰리프":
        embed = discord.Embed(title="Cherif", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="탄창 장탄 수", value="6")
        embed.add_field(name="주 공격", value="- 반자동 사격\n- 연사 속도: 초당 4발", inline=False)
        await ctx.send(embed=embed)
        return 

    await ctx.send("해당되는 무기 정보를 찾을 수 없습니다!")

@client.command()
async def 에이전트(ctx, name):

    if name == "브림스톤":
        embed = discord.Embed(title="Brimstone", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="소이탄", value="소이탄 발사기를 장착합니다. 발사하면 바닥에 떨어졌을 때 폭발하는 소이탄을 날려 적에게 피해를 입히는 화염 구역을 생성합니다. 생성된 구역은 일정 시간 유지됩니다.")
        embed.add_field(name="공중 연막", value="전술 지도를 장착합니다. 발사하면 브림스톤의 연막을 퍼뜨릴 위치를 설정합니다. 보조 공격 시 위치 확정 후 연막을 날려 한동안 선택한 지역의 시야를 차단합니다.", inline=False)
        embed.add_field(name="자극제 신호기", value="자극제 신호기를 장착합니다. 발사하면 브림스톤 앞에 자극제 신호기를 던집니다. 신호기가 떨어진 곳에는 플레이어에게 속사 효과를 부여하는 영역이 생성됩니다.", inline=False)
        embed.add_field(name="궤도 일격", value="전술 지도를 장착합니다. 발사하면 선택한 위치에 궤도 일격 레이저를 쏘아 해당 영역에 있는 플레이어에게 큰 지속 피해를 입힙니다.", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713365220462035024/brimstone.png")
        await ctx.send(embed=embed)
        return 
    if name == "세이지":
        embed = discord.Embed(title="Sage", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="둔화 구슬", value="둔화 구슬을 장착합니다. 발사하면 땅에 닿은 후 폭발하여 일정 시간 동안 둔화 영역을 생성하는 구슬을 던집니다. 둔화 영역에 있는 플레이어는 속도가 느려집니다.", inline=False)
        embed.add_field(name="회복 구슬", value="회복 구슬을 장착합니다. 피해를 입은 아군을 조준한 후 발사하면 해당 아군이 서서히 체력을 회복합니다. 세이지가 피해를 입었을 때 보조 공격 시 자신의 체력을 서서히 회복합니다.", inline=False)
        embed.add_field(name="장벽 구슬", value="장벽 구슬을 장착합니다. 발사하면 단단한 장벽을 설치합니다. 보조 공격 시 장벽이 회전합니다.", inline=False)
        embed.add_field(name="부활", value="부활 스킬을 장착합니다. 죽은 아군을 조준한 후 발사하면 해당 아군이 부활하기 시작합니다. 짧은 정신 집중이 끝나면 아군이 최대 체력으로 되살아납니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713366025768403035/sage.png")
        await ctx.send(embed=embed)
        return 
    if name == "소바":
        embed = discord.Embed(title="Sova", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="충격 화살", value="충격 화살을 발사하는 활을 장착합니다. 발사하면 충돌 시 폭발하여 주변 플레이어에게 피해를 입히는 화살을 전방으로 날립니다. 발사를 길게 누르면 화살의 사거리가 늘어납니다. 보조 공격 시 화살이 최대 두 번 더 튕깁니다.", inline=False)
        embed.add_field(name="정찰용 화살", value="정찰 화살을 발사하는 활을 장착합니다. 발사하면 정찰 화살을 전방으로 날려 화살이 꽂힌 곳을 기준으로 모습이 드러난 주변 적의 위치를 표시합니다. 적이 이 화살을 파괴할 수 있습니다. 발사를 길게 누르면 화살의 사거리가 늘어납니다. 보조 공격 시 화살이 최대 두 번 더 튕깁니다.", inline=False)
        embed.add_field(name="올빼미 드론", value="올빼미 드론을 장착합니다. 발사하면 드론을 날려 조종합니다. 드론을 조종하는 동안 발사를 누르면 표식용 다트가 발사됩니다. 다트에 맞은 플레이어는 위치가 드러납니다.", inline=False)
        embed.add_field(name="사냥꾼의 분노", value="벽을 관통하는 에너지 3개를 장거리로 발사하는 활을 장착합니다. 발사하면 전방에 일직선상으로 에너지를 날려 닿은 적에게 피해를 입히고 위치를 드러냅니다. 스킬 지속시간이 활성화된 상태에서 최대 두 번 더 다시 사용할 수 있습니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713366707393265704/sova.png")
        await ctx.send(embed=embed)
        return 
    if name == "제트":
        embed = discord.Embed(title="Jett", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="상승 기류", value="제트가 즉시 높이 날아오릅니다.")
        embed.add_field(name="순풍", value="제트가 즉시 이동 방향으로 빠르게 이동합니다. 제트가 가만히 서 있을 경우에는 앞으로 빠르게 이동합니다.", inline=False)
        embed.add_field(name="연막 폭발", value="표면에 닿아 충격을 받으면 구름으로 팽창해 잠시 시야를 가리는 투사체를 즉시 던집니다. 스킬 키를 길게 누르면 연기가 조준점 방향으로 휘어집니다.", inline=False)
        embed.add_field(name="칼날 폭풍", value="명중률이 높으며 적 처치 시 다시 충전되는 투척용 단검을 장착합니다. 발사하면 대상에게 단검 하나를 던집니다. 보조 공격 시 대상에게 남은 단검을 전부 던집니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713367488070680687/jett.png")
        await ctx.send(embed=embed)
        return 
    if name == "피닉스":
        embed = discord.Embed(title="Phoenix", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="커브볼", value="던지면 휘어져 날아간 후 곧 폭발하는 섬광 구슬을 장착합니다. 발사하면 섬광 구슬이 왼쪽으로 휘어지며 폭발합니다. 이때 구슬을 바라보는 플레이어는 전부 실명합니다. 보조 공격 시 섬광 구슬이 오른쪽으로 휘어집니다.", inline=False)
        embed.add_field(name="뜨거운 손", value="화염구를 장착합니다. 발사하면 일정 시간이 지나거나 땅에 닿은 후 폭발하는 화염구를 던집니다. 폭발 지점에는 일정 시간 유지되는 화염 구역이 생성되어 적에게 피해를 입힙니다.", inline=False)
        embed.add_field(name="불길", value="화염 장벽을 장착합니다. 발사하면 앞으로 이동하는 여러 개의 화염을 일렬로 생성하여 시야를 차단하고 통과하는 플레이어에게 피해를 입히는 화염 장벽을 생성합니다. 발사를 길게 누르면 조준점 방향으로 장벽 궤적을 바꿉니다.", inline=False)
        embed.add_field(name="역습", value="즉시 피닉스의 위치에 표식을 놓습니다. 스킬 사용 도중 죽거나 지속시간이 끝나면 해당 위치에서 최대 체력으로 부활합니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713368103035076658/phoenix.png")
        await ctx.send(embed=embed)
        return 
    if name == "레이즈":
        embed = discord.Embed(title="Raze", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="폭발 팩", value="표면에 부착되는 폭발 팩을 던집니다. 부착 후 다시 사용하면 팩이 폭발하며 적중한 대상에게 피해를 입히고 밀어냅니다.", inline=False)
        embed.add_field(name="페인트탄", value="집속탄을 장착합니다. 발사하면 집속탄을 던집니다. 집속탄은 피해를 입히고 여러 개의 자탄을 퍼뜨립니다. 자탄은 각각의 범위 내에 있는 모든 대상에게 피해를 입힙니다.", inline=False)
        embed.add_field(name="폭발 봇", value="폭발 봇을 장착합니다. 발사하면 폭발 봇이 지면에서 일직선으로 이동하며 벽을 만나면 튕겨 나옵니다. 폭발 봇의 정면 원뿔형 시야 안에 적이 포착되면 해당 적에게 돌진하며 폭발해 치명적인 피해를 입힙니다.", inline=False)
        embed.add_field(name="대미 장식", value="로켓 발사기를 장착합니다. 발사하면 충돌 시 대량의 범위 피해를 입히는 로켓을 발사합니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713368739940401152/raze.png")
        await ctx.send(embed=embed)
    if name == "바이퍼":
        embed = discord.Embed(title="Viper", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="독성 연기", value="가스 방사기를 장착합니다. 발사하면 라운드 내내 유지되는 방사기를 던집니다. 스킬을 다시 사용하면 연료를 소모해 독성 가스 구름을 만듭니다. 이 스킬은 여러 번 재사용이 가능하여 주운 후 다시 배치할 수 있습니다.")
        embed.add_field(name="독성 장막", value="가스 방사기 발사기를 장착합니다. 발사하면 여러 개의 가스 방사기를 일렬로 길게 배치합니다. 스킬을 다시 사용하면 연료를 소모해 높은 독성 연기 장벽을 생성합니다. 이 스킬은 여러 번 재사용이 가능합니다.", inline=False)
        embed.add_field(name="뱀 이빨", value="화학 물질 발사기를 장착합니다. 발사하면 바닥에 떨어졌을 때 폭발하는 통을 날립니다. 통은 폭발하며 적에게 피해를 입히고 둔화시키는 화학 물질 지역을 일정 시간 동안 생성합니다.", inline=False)
        embed.add_field(name="독사의 구덩이", value="화학 물질 분사기를 장착합니다. 발사하면 사방으로 화학 물질 연기를 분사해 안에 있는 플레이어의 가시거리와 최대 체력을 감소시키는 거대 연기를 생성합니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713370057430007868/viper.png")
        await ctx.send(embed=embed)
        return 
    if name == "브리치":
        embed = discord.Embed(tilte="Breach", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="섬광 폭발", value="실명탄을 장착합니다. 발사하면 벽을 통과하고 빠르게 효과가 발생하는 폭발을 일으켜 섬광을 본 모든 플레이어를 실명시킵니다.")
        embed.add_field(name="균열", value="지진파를 장착합니다. 발사를 길게 누르면 사거리가 늘어납니다. 키를 떼면 지진파를 날려 경로상에 있는 적과 대상 범위 내의 모든 적을 멍하게 합니다.", inline=False)
        embed.add_field(name="여진", value="융합 에너지탄을 장착합니다. 발사하면 벽을 통과하고 느리게 효과가 발생하는 폭발을 일으켜 대상 범위 내의 모든 적에게 큰 피해를 입힙니다.", inline=False)
        embed.add_field(name="지진 강타", value="지진탄을 장착합니다. 발사하면 모든 지형을 통과하는 지진 파동을 날려 경로상에 있는 모든 적을 멍하게 하고 공중으로 띄웁니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713370458694877194/breach.png")
        await ctx.send(embed=embed)
        return 
    if name == "사이퍼":
        embed = discord.Embed(title="Cypher", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="사이버 감옥", value="사이버 감옥을 장착합니다. 발사하면 사이퍼 앞에 사이버 감옥을 던집니다. 활성화하면 시야를 차단하고 지나가는 적을 둔화시키는 구역이 생성됩니다.")
        embed.add_field(name="스파이캠", value="스파이캠을 장착합니다. 발사하면 지정 위치에 스파이캠을 설치합니다. 스킬을 다시 사용하면 카메라 화면을 조작할 수 있습니다. 카메라를 조작하는 동안 발사를 누르면 표식용 다트가 발사됩니다. 다트에 맞은 플레이어는 위치가 드러납니다.", inline=False)
        embed.add_field(name="함정", value="함정을 장착합니다. 발사하면 지정 위치에 파괴 가능한 위장 함정을 설치하여 설치 위치와 반대쪽 벽 사이를 연결하는 선을 생성합니다. 함정을 넘어가는 적 플레이어는 제때 장치를 파괴하지 않으면 잠시 후 속박되어 위치가 드러나며 멍해집니다. 이 스킬은 회수하여 다시 설치할 수 있습니다.", inline=False)
        embed.add_field(name="신경 절도", value="적 플레이어가 처치된 즉시 조준한 후 사용하면 생존한 모든 적 플레이어의 위치가 드러납니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713370830377058374/cypher.png")
        await ctx.send(embed=embed)
        return 
    if name == "오멘":
        embed = discord.Embed(title="Omen", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="피해망상", value="즉시 앞으로 그림자 투사체를 발사해 투사체에 닿은 모든 플레이어의 가시거리를 잠시 감소시킵니다. 이 투사체는 벽을 통과할 수 있습니다.", inline=False)
        embed.add_field(name="어둠의 장막", value="그림자 구슬을 장착하고 사거리를 표시합니다. 발사하면 표시한 위치에 그림자 구슬을 던져 한동안 시야를 차단하는 그림자 영역을 생성합니다. 조준 시 보조 공격을 길게 누르면 표시 위치를 더 멀리 옮깁니다. 조준 시 스킬 키를 길게 누르면 표시 위치를 더 가까이 옮깁니다.")
        embed.add_field(name="어둠의 발자국", value="그림자 걸음 스킬을 장착하고 사거리를 표시합니다. 발사하면 짧은 정신 집중 후 표시한 위치로 순간 이동합니다. 적들은 출발 지점에서 들리는 소리만 들을 수 있습니다.", inline=False)
        embed.add_field(name="그림자 습격", value="전술 지도를 장착합니다. 발사하면 선택한 위치로 순간 이동을 시작합니다. 순간 이동 중에는 오멘이 그림자로 나타나며 이때 적이 그림자를 파괴하면 순간 이동이 취소됩니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/713330037943828520/713371253209038878/omen.png")
        await ctx.send(embed=embed)
        return 
    if name == "레이나":
        embed = discord.Embed(title="Reina", color=discord.Colour.from_rgb(47, 49, 54))
        embed.add_field(name="포식", value="영혼 수확: 레이나가 처치한 적은 3초 동안 유지되는 영혼 구슬을 남깁니다. 포식: 즉시 근처에 있는 영혼 구슬을 흡수하여 짧은 시간 동안 순식간에 체력을 회복합니다. 이 스킬로 회복한 체력이 100을 넘어가면 초과분은 시간이 흐르면서 사라집니다. 여제 활성화 시 이 스킬이 자동으로 사용되며 영혼 구슬을 흡수하지 않습니다.", inline=False)
        embed.add_field(name="무시", value="즉시 근처에 있는 영혼 구슬을 흡수하여 짧은 시간 동안 무형 상태가 됩니다. 여제 활성화 시 추가로 투명 상태가 됩니다.")
        embed.add_field(name="눈총", value="파괴 가능한 천상의 눈을 장착합니다. 활성화하면 눈을 짧게 앞으로 던집니다. 눈을 본 적은 모두 시야가 제한됩니다.", inline=False)
        embed.add_field(name="여제", value="즉시 광란 상태가 되어 사격, 장착, 재장전 속도가 크게 증가합니다. 영혼 수확의 충전량을 무제한으로 얻습니다. 적을 처치하면 지속시간이 초기화됩니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/717356740777345119/717357507668082749/reyna.png")
        await ctx.send(embed=embed)
        return 

    await ctx.send("해당 에이전트 정보를 찾을 수 없습니다.")

@client.command()
async def 맵(ctx, name):

    if name == "헤이븐":
        await ctx.send("https://cdn.discordapp.com/attachments/713330037943828520/713361624898994329/7aebda79a73ffa04.png")
        return 
    if name == "바인드":
        await ctx.send("https://cdn.discordapp.com/attachments/713330037943828520/713361749512028170/fc55ed1e3bba76e2.png")
        return 
    if name == "스플릿":
        await ctx.send("https://cdn.discordapp.com/attachments/713330037943828520/713361826414460928/26f4c0b943e24993.png")
        return 

    await ctx.send("해당 맵을 찾을 수 없습니다.")

@client.command()
async def 패치(ctx):

    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://beta.playvalorant.com/ko-kr/news/'
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    
    embed = discord.Embed(title="https://beta.playvalorant.com/ko-kr/news/", color=discord.Colour.from_rgb(47, 49, 54))

    for i in range(0, 10):

        news1 = bsObj.find('div', {'class': 'NewsArchive-module--content--_kqJU'}).find_all('div', {'class': 'NewsArchive-module--newsCardWrapper--2OQiG'})
        news2 = news1[i]

        news3 = news2.find('h5', {'class': 'heading-05 NewsCard-module--title--1MoLu'}).text 
        news4 = news2.find('p', {'class': 'copy-02 NewsCard-module--description--3sFiD'}).text 

        embed.add_field(name=news3, value=news4, inline=False)

    await ctx.send(embed=embed)
            
client.run('NzEzMzIwNzAzMTU1MzcyMDc0.XseZuw.LJJ1nbIG9CRuzlFJl-08aUsyWPU')