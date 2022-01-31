import discord
from discord.ext import commands
import configparser  

config = configparser.ConfigParser() 
config.read("settings.ini")

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Я запущен!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="пророка"))

# @bot.command(name='list', description='узнать кол-во игроков на сервере', help='узнать кол-во игроков на сервере', aliases=['l','online'])
# async def list(ctx):
#     F = open('list.txt')
#     str1 = F.readline() 
#     str2 = F.readline() 
#     await ctx.send(str1 + str2)

@bot.command() 
async def sex(ctx):
    await ctx.send('ай ай ай, я все маме расскажу!')

@bot.command() 
async def info(ctx):
    await ctx.send('version: 1.0.1\nlang: ' + config['lang']['lang'] + '\nmade by prorok ')


bot.run('OTM3NzA0идинахуйMDE4Njg5MDQ0.YffngA.Xps') 
