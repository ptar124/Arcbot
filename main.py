import discord
from itertools import cycle
from discord.ext import commands, tasks
from keep_alive import keep_alive
from randfunc import randfunc
from cuslistfunc import cuslistfunc
from combinefunc import combinefunc
from judgefunc import hardfunc, exhardfunc
from helpfunc import helpfunc
import os

#bot = discord.Client()
bot = commands.Bot(command_prefix="$")
bot.remove_command('help')

@bot.event
async def on_ready():
  change_status.start()
  uptime_message.start()
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def rand(ctx, *, arg):
	await randfunc(ctx, arg)

@bot.command()
async def cuslist(ctx, *, arg):
	await cuslistfunc(ctx, arg)

@bot.command()
async def combine(ctx, code1, op, code2):
  await combinefunc(ctx, code1, op, code2)

@bot.command()
async def hard(ctx, s, p, f, l):
	await hardfunc(ctx, s, p, f, l)

@bot.command()
async def exhard(ctx, s, p, f, l):
	await exhardfunc(ctx, s, p, f, l)
	
@bot.command()
async def chuni(ctx, s, p, f, l):
	await chunifunc(ctx, s, p, f, l)

@bot.command()
async def help(ctx, arg=""):
	await helpfunc(ctx, arg)

keep_alive()

status = cycle(['$help for info','ping ptar if down'])
uptime = 0

@tasks.loop(seconds=10)
async def change_status():
    global uptime
    uptime = uptime + 10
    await bot.change_presence(activity=discord.Game(next(status)))

@tasks.loop(seconds=3600)
async def uptime_message():
    global uptime
    print("bot up for:" + str(uptime))

bot.run(os.getenv('TOKEN'))
