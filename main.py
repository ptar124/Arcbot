import discord
from discord.ext import commands
from keep_alive import keep_alive
from randfunc import randfunc
import os

#bot = discord.Client()
bot = commands.Bot(command_prefix = "!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def rand(ctx, *, arg):
    randfunc(ctx, arg)


@bot.command()
async def cuslist(ctx, *, arg):

    global customlist

    if arg == "reset":
        print("Custom list reset.")
        await ctx.channel.send("Custom list reset.")
        customlist = []
    
    elif arg.startswith("rm"):
        if arg.startswith("dup", 3):
            customlist = list(set(customlist))
            await ctx.channel.send("Duplicate elements removed")

        elif arg[3:].isnumeric():
            await ctx.channel.send("Removed ``" + customlist[int(arg[3:])-1].gettitle() + "`` from custom list")
            customlist.pop(int(arg[3:])-1)
        else:
            await ctx.channel.send("Invalid song number")

    elif arg[0:4] == "view":
        customlistview = "**Current song list:** ```"
        customlistview2 = "**Current song list:** ```"
        customlistview3 = "**Current song list:** ```"
        x = 0
        while x < len(customlist):
            if len(customlistview) < 1800:
               customlistview = customlistview + str(x+1) + ". " + customlist[x].gettitle() + " \n"
            else:
                if len(customlistview2) < 1800:
                    customlistview2 = customlistview2 + str(x+1) + ". " + customlist[x].gettitle() + " \n"
                else:
                    customlistview3 = customlistview3 + str(x+1) + ". " + customlist[x].gettitle() + " \n"
            x = x+1
                
        customlistview = customlistview + "``` To remove songs, use ``cuslist rm [song number]``"
        customlistview2 = customlistview2 + "``` To remove songs, use ``cuslist rm [song number]``"
        customlistview3 = customlistview3 + "``` To remove songs, use ``cuslist rm [song number]``"

        if len(customlistview2) != len(customlistview3):
            await ctx.channel.send("The list exceeds Discord's character limit and has been truncated. Use ``cuslist view [page number]``")
        
        if customlist == []:
            await ctx.channel.send("You can't view an empty list!")

        elif arg.startswith("2", 5):
            await ctx.channel.send(customlistview2)

        elif arg.startswith("3", 5):
            await ctx.channel.send(customlistview3)
        else:
            await ctx.channel.send(customlistview)
    
    elif arg.startswith("filter"):
        oparg = str(arg[11:12])
        diffarg = float(arg[13:])

        if diffarg > 0 and diffarg < 12:
            if arg.startswith("pst", 7):
                if oparg == "=":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getpstdiff() != diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getpstdiff() >= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getpstdiff() <= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
            elif arg.startswith("prs", 7):
                if oparg == "=":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getprsdiff() != diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getprsdiff() >= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getprsdiff() <= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
            elif arg.startswith("ftr", 7):
                if oparg == "=":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getftrdiff() != diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getftrdiff() >= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getftrdiff() <= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                else:
                    await ctx.channel.send("Invalid difficulty, level, or operation")
            elif arg.startswith("byd", 7):
                if oparg == "=":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getbyddiff() != diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getbyddiff() >= diffarg or customlist[x].getbyddiff() < 1:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getbyddiff() <= diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
            else:
                await ctx.channel.send("Invalid difficulty, level, or operation")

            await ctx.channel.send("Applied Filter: " + arg[7:10] + " " + oparg + " " + str(diffarg) + "\n**This feature is still experimental, please double check the list**")

        else:
            await ctx.channel.send("Invalid difficulty, level, or operation")


    elif arg.startswith("addpack"):
        packname = arg[8:]
        if packname == "all":
            customlist = customlist + songlist
            print("All Songs added to custom list")
            await ctx.channel.send("All Songs added to custom list")

        elif packname == "free":
            customlist = customlist + freelist
            print("All Free Songs added to custom list")
            await ctx.channel.send("All Free Songs added to custom list")

        elif packname == "ma":
            customlist = customlist + memoryarchivelist
            print("All Memory Archive Songs added to custom list")
            await ctx.channel.send("All Memory Archive Songs added to custom list")

        elif packname == "arc":
            customlist = customlist + arcaealist
            print("All Arcaea Pack Songs added to custom list")
            await ctx.channel.send("All Arcaea Pack Songs added to custom list")

        elif packname == "we":
            customlist = customlist + worldextendlist
            print("All World Extend Songs added to custom list")
            await ctx.channel.send("All World Extend Songs added to custom list")

        elif packname == "bf":
            customlist = customlist + blackfatelist
            print("All Black Fate Songs added to custom list")
            await ctx.channel.send("All Black Fate Songs added to custom list")

        elif packname == "ap":
            customlist = customlist + adversepreludelist
            print("All Adverse Prelude Songs added to custom list")
            await ctx.channel.send("All Adverse Prelude Songs added to custom list")

        elif packname == "ls":
            customlist = customlist + luminousskylist
            print("All Luminous Sky Songs added to custom list")
            await ctx.channel.send("All Luminous Sky Songs added to custom list")

        elif packname == "vl":
            customlist = customlist + viciouslabyrinthlist
            print("All Vicious Labyrinth Songs added to custom list")
            await ctx.channel.send("All Vicious Labyrinth Songs added to custom list")

        elif packname == "ec":
            customlist = customlist + eternalcorelist
            print("All Eternal Core Songs added to custom list")
            await ctx.channel.send("All Eternal Core Songs added to custom list")

        elif packname == "ep":
            customlist = customlist + ephemeralpagelist + thejourneyonwardslist
            print("All Ephemeral Page Songs added to custom list")
            await ctx.channel.send("All Ephemeral Page Songs added to custom list")

        elif packname == "ep -append":
            customlist = customlist + ephemeralpagelist
            print("All Ephemeral Page Songs added to custom list")
            await ctx.channel.send("All Ephemeral Page Songs added to custom list -append")

        elif packname == "tjo" or packname == "ep append":
            customlist = customlist + thejourneyonwardslist
            print("All The Journey Onwards Songs added to custom list")
            await ctx.channel.send("All The Journey Onwards Songs added to custom list")

        elif packname == "eo":
            customlist = customlist + esotericorderlist + paletapestrylist
            print("All Esoteric Order Songs added to custom list")
            await ctx.channel.send("All Esoteric Order Songs added to custom list")

        elif packname == "eo -append":
            customlist = customlist + esotericorderlist
            print("All Esoteric Order Songs added to custom list")
            await ctx.channel.send("All Esoteric Order Songs added to custom list -append")

        elif packname == "pt" or packname == "eo append":
            customlist = customlist + paletapestrylist
            print("All Pale Tapestry Songs added to custom list")
            await ctx.channel.send("All Pale Tapestry Songs added to custom list")

        elif packname == "sr":
            customlist = customlist + sunsetradiancelist
            print("All Sunset Radiance Songs added to custom list")
            await ctx.channel.send("All Sunset Radiance Songs added to custom list")

        elif packname == "ar":
            customlist = customlist + absolutereasonlist
            print("All Absolute Reason Songs added to custom list")
            await ctx.channel.send("All Absolute Reason Songs added to custom list")

        elif packname == "be":
            customlist = customlist + binaryenfoldlist
            print("All Binary Enfold Songs added to custom list")
            await ctx.channel.send("All Binary Enfold Songs added to custom list")

        elif packname == "av":
            customlist = customlist + ambivalentvisionlist
            print("All Ambivalent Vision Songs added to custom list")
            await ctx.channel.send("All Ambivalent Vision Songs added to custom list")

        elif packname == "cs":
            customlist = customlist + crimsonsolacelist
            print("All Crimsone Solace Songs added to custom list")
            await ctx.channel.send("All Crimson Solace Songs added to custom list")

        elif packname == "mai":
            customlist = customlist + maimailist
            print("All maimai Songs added to custom list")
            await ctx.channel.send("All maimai Songs added to custom list")

        elif packname == "ong":
            customlist = customlist + ongekilist
            print("All O.N.G.E.K.I. Songs added to custom list")
            await ctx.channel.send("All O.N.G.E.K.I. Songs added to custom list")

        elif packname == "chu":
            customlist = customlist + chunithmlist + chunithm2list
            print("All CHUNITHM Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Songs added to custom list")

        elif packname == "chu -append":
            customlist = customlist + chunithmlist
            print("All CHUNITHM Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Songs added to custom list")

        elif packname == "chu2" or packname == "chu append":
            customlist = customlist + chunithm2list
            print("All CHUNITHM Chapter 2 Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Chapter 2 Songs added to custom list")

        elif arg.startswith("gc", 8):
            customlist = customlist + groovecoasterlist
            print("All Groove Coaster Songs added to custom list")
            await ctx.channel.send("All Groove Coaster Songs added to custom list")

        elif arg.startswith("ts", 8):
            customlist = customlist + tonespherelist
            print("All Tone Sphere Songs added to custom list")
            await ctx.channel.send("All Tone Sphere Songs added to custom list")

        elif arg.startswith("lan", 8):
            customlist = customlist + lanotalist
            print("All Lanota Songs added to custom list")
            await ctx.channel.send("All Lanota Songs added to custom list")

        elif arg.startswith("dnx", 8):
            customlist = customlist + adversepreludelist
            print("All Dynamix Songs added to custom list")
            await ctx.channel.send("All Dynamix Songs added to custom list")

        else:
            await ctx.channel.send("Invalid pack or song name")
    else:
        print("Invalid argument for command $cuslist")
        await ctx.channel.send('Invalid argument for command $cuslist')


@bot.command()
async def hard(ctx, s, p, f, l):
    shiny = float(s)
    pure = float(p) - float(s)
    far = float(f)
    lost = float(l)
    ncount = shiny + pure + far + lost
    sscore = 10000000/ncount
    pscore = sscore*(0.6)
    fscore = sscore*(0.2)
    total = shiny*sscore + pure*pscore + far*fscore
    grade = ""

    if total > 10000000:
        grade = ":place_of_worship: :place_of_worship: :place_of_worship: wait how did you get over 10m, please check your inputs!"
    elif total == 10000000:
        grade = ":regional_indicator_m: :regional_indicator_p: :regional_indicator_m: :tada:"
    elif total >= 9900000:
        grade = ":regional_indicator_e: :regional_indicator_x: :arrow_double_up:"
    elif total >= 9800000:
        grade = ":regional_indicator_e: :regional_indicator_x:"
    elif total >= 9500000:
        grade = ":a: :a:"
    elif total >= 9200000:
        grade = ":a:"
    elif total >= 8900000:
        grade = ":b:"
    elif total >= 8600000:
        grade = ":regional_indicator_c:"
    else:
        grade = ":regional_indicator_f:"

    await ctx.channel.send("Hard Judge Score:\n" + grade + "  **" + str(total) + "**")

@bot.command()
async def exhard(ctx, s, p, f, l):
    shiny = float(s)
    pure = float(p) - float(s)
    far = float(f)
    lost = float(l)
    ncount = shiny + pure + far + lost
    sscore = 10000000/ncount
    pscore = sscore*(0.5)
    fscore = 0
    total = shiny*sscore + pure*pscore + far*fscore
    grade = ""

    if total > 10000000:
        grade = ":place_of_worship: :place_of_worship: :place_of_worship: wait how did you get over 10m, please check your inputs!"
    elif total == 10000000:
        grade = ":regional_indicator_m: :regional_indicator_p: :regional_indicator_m: :tada:"
    elif total >= 9900000:
        grade = ":regional_indicator_e: :regional_indicator_x: :arrow_double_up:"
    elif total >= 9800000:
        grade = ":regional_indicator_e: :regional_indicator_x:"
    elif total >= 9500000:
        grade = ":a: :a:"
    elif total >= 9200000:
        grade = ":a:"
    elif total >= 8900000:
        grade = ":b:"
    elif total >= 8600000:
        grade = ":regional_indicator_c:"
    else:
        grade = ":regional_indicator_f:"

    await ctx.channel.send("EXTRA Hard Judge Score:\n" + grade + "  **" + str(total) + "**")

@bot.command()
async def help (ctx, arg = ""):
    helpstr = ""
    if arg == "rand":
        await ctx.channel.send("``rand [pack]`` - Randomizes songs from a specific pack. The  ``free`` pack is pre-made for convenience for F2P players.")
    elif arg == "cuslist":
        await ctx.channel.send("``cuslist addpack [pack]`` - Add a pack to the custom list, you can add a pack more than once.\n``cuslist rm [int]`` - Remove a song from the list, song number is shown using ``cuslist view``. To remove duplicates, use ``dup`` instead of a number\n``cuslist view`` - View the custom list\n``cuslist reset`` - Reset the custom list to an empty list\n``cuslist filter [difficulty] [operator] [level]`` Filter only specific difficulties, supported operators are ``>``, ``<``, and ``=``. For ``X+`` difficulties, use ``X.7``. **Note the spaces between arguments**")
    elif arg == "hard":
        await ctx.channel.send("``hard [shiny] [pure] [far] [lost]`` - A harder judge for shiny acc battling, uses RAVON's ratio of 5:3:1:0")
    elif arg == "exhard":
        await ctx.channel.send("``exhard [shiny] [pure] [far] [lost]`` - An even harder judge for shiny acc battling, pures are worth half of shinies, fars and below don't count")
    elif arg == "pack":
        await ctx.channel.send("``all`` - All Songs\n``free`` - All Free Songs (Arcaea + World Extend)\n``ma`` - Memory Archive\n``arc`` - Arcaea\n``we`` - World Extend\n``bf`` - Black Fate\n``ap`` - Adverse Prelude\n``ls`` - Luminous Sky\n``vl`` - Vicious Labyrinth\n``ec`` - Eternal Core\n``sr`` - Sunset Radiance\n``ar`` - Absolute Reason\n``be`` - Binary Enfold\n``av`` - Ambivalent Vision\n``cs`` - Crimson Solace\n``ep`` - Ephemeral Page\n``eo`` - Esoteric Order\n``mai`` - maimai\n``ong`` - O.N.G.E.K.I\n``chu`` - CHUNITHM\n``gc`` - Groove Coaster\n``lan`` - Lanota\n``dnx`` - Dynamix\n``cus`` - Custom List")
    else:
        helpstr = "Current Arcbot Commands:```\nrand\ncuslist\nhard\nexhard```"
        helpstr = helpstr + "For more information on each command, type ``$help [command]`` or for pack abbrieviations, type ``$help pack``"
        await ctx.channel.send(helpstr)

keep_alive()
bot.run(os.getenv('TOKEN'))