import discord
from discord.ext import commands
from keep_alive import keep_alive
from randfunc import randfunc
from cuslistfunc import cuslistfunc
from judgefunc import hardfunc
from judgefunc import exhardfunc
from helpfunc import helpfunc
import os

#bot = discord.Client()
bot = commands.Bot(command_prefix = "!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def rand(ctx, *, arg):
    await randfunc(ctx, arg)

@bot.command()
async def cuslist(ctx, *, arg):
    await cuslistfunc(ctx, arg)

@bot.command()
async def hard(ctx, s, p, f, l):
    await hardfunc(ctx, s, p, f, l)

@bot.command()
async def exhard(ctx, s, p, f, l):
    await exhardfunc(ctx, s, p, f, l)
    
@bot.command()
async def help (ctx, arg = ""):
    await helpfunc(ctx, arg)

keep_alive()
bot.run(os.getenv('TOKEN'))