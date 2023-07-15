import discord
from discord.ext import commands
import googletrans

token = "************************************************************************"
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

translator = googletrans.Translator()

def trans_ko(translator, src):
    return(translator.translate(src, dest='ko').text)

def trans_en(translator, src):
    return(translator.translate(src, dest='en').text)

def trans_jp(translator, src):
    return(translator.translate(src, dest='ja').text)

def trans_hk(translator, src):
    return(translator.translate(src, dest='zh-tw').text)

def trans_cn(translator, src):
    return(translator.translate(src, dest='zh-cn').text)

def trans_es(transaltor, src):
    return(translator.translate(src, dest='es').text)

@bot.event
async def on_ready():
    print("bot is ready\n")

@bot.event
async def on_reaction_add(reaction, user):
    print(f'{user}님이 {reaction}으로 반응했습니다')
    channel = reaction.message.channel
    text = reaction.message.content
    mention = user.mention
    if str(reaction) == "🇰🇷":
        result = trans_ko(translator, text)
        await channel.send(f'{mention} : {result}')
    elif str(reaction) == "🇯🇵":
        result = trans_jp(translator, text)
        await channel.send(f'{mention} : {result}')
    elif str(reaction) == "🇺🇸":
        result = trans_en(translator, text)
        await channel.send(f'{mention} : {result}')
    elif str(reaction) == "🇨🇳":
        result = trans_cn(translator, text)
        await channel.send(f'{mention} : {result}')
    elif str(reaction) == "🇭🇰":
        result = trans_hk(translator, text)
        await channel.send(f'{mention} : {result}')
    elif str(reaction) in ["🇪🇸", "🇲🇽", "🇦🇷"]:
        result = trans_es(translator, text)
        await channel.send(f'{mention} : {result}')

bot.run(token)

