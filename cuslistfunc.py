import songs

async def cuslistfunc(ctx, arg):

    if arg == "reset":
        print("Custom list reset.")
        await ctx.channel.send("Custom list reset.")
        songs.customlist = []
    
    elif arg.startswith("rm"):
        if arg.startswith("dup", 3):
            songs.customlist = list(set(songs.customlist))
            await ctx.channel.send("Duplicate elements removed")

        elif arg[3:].isnumeric():
            await ctx.channel.send("Removed ``" + songs.customlist[int(arg[3:])-1].gettitle() + "`` from custom list")
            songs.customlist.pop(int(arg[3:])-1)
        else:
            await ctx.channel.send("Invalid song number")

    elif arg[0:4] == "view":
        customlistview = "**Current song list:** ```"
        customlistview2 = "**Current song list:** ```"
        customlistview3 = "**Current song list:** ```"
        x = 0
        while x < len(songs.customlist):
            if len(customlistview) < 1800:
               customlistview = customlistview + str(x+1) + ". " + songs.customlist[x].gettitle() + " \n"
            else:
                if len(customlistview2) < 1800:
                    customlistview2 = customlistview2 + str(x+1) + ". " + songs.customlist[x].gettitle() + " \n"
                else:
                    customlistview3 = customlistview3 + str(x+1) + ". " + songs.customlist[x].gettitle() + " \n"
            x = x+1
                
        customlistview = customlistview + "``` To remove songs, use ``cuslist rm [song number]``"
        customlistview2 = customlistview2 + "``` To remove songs, use ``cuslist rm [song number]``"
        customlistview3 = customlistview3 + "``` To remove songs, use ``cuslist rm [song number]``"

        if len(customlistview2) != len(customlistview3):
            await ctx.channel.send("The list exceeds Discord's character limit and has been truncated. Use ``cuslist view [page number]``")
        
        if songs.customlist == []:
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
                    while x < len(songs.customlist):
                        if songs.customlist[x].getpstdiff() != diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getpstdiff() >= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getpstdiff() <= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
            elif arg.startswith("prs", 7):
                if oparg == "=":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getprsdiff() != diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getprsdiff() >= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getprsdiff() <= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
            elif arg.startswith("ftr", 7):
                if oparg == "=":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getftrdiff() != diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getftrdiff() >= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getftrdiff() <= diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                else:
                    await ctx.channel.send("Invalid difficulty, level, or operation")
            elif arg.startswith("byd", 7):
                if oparg == "=":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getbyddiff() != diffarg:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == "<":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getbyddiff() >= diffarg or songs.customlist[x].getbyddiff() < 1:
                            songs.customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(songs.customlist):
                        if songs.customlist[x].getbyddiff() <= diffarg:
                            songs.customlist.pop(x)
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
            songs.customlist = songs.customlist + songs.songlist
            print("All Songs added to custom list")
            await ctx.channel.send("All Songs added to custom list")

        elif packname == "free":
            songs.customlist = songs.customlist + songs.freelist
            print("All Free Songs added to custom list")
            await ctx.channel.send("All Free Songs added to custom list")

        elif packname == "ma":
            songs.customlist = songs.customlist + songs.memoryarchivelist
            print("All Memory Archive Songs added to custom list")
            await ctx.channel.send("All Memory Archive Songs added to custom list")

        elif packname == "arc":
            songs.customlist = songs.customlist + songs.arcaealist
            print("All Arcaea Pack Songs added to custom list")
            await ctx.channel.send("All Arcaea Pack Songs added to custom list")

        elif packname == "we":
            songs.customlist = songs.customlist + songs.worldextendlist
            print("All World Extend Songs added to custom list")
            await ctx.channel.send("All World Extend Songs added to custom list")

        elif packname == "bf":
            songs.customlist = songs.customlist + songs.blackfatelist
            print("All Black Fate Songs added to custom list")
            await ctx.channel.send("All Black Fate Songs added to custom list")

        elif packname == "ap":
            songs.customlist = songs.customlist + songs.adversepreludelist
            print("All Adverse Prelude Songs added to custom list")
            await ctx.channel.send("All Adverse Prelude Songs added to custom list")

        elif packname == "ls":
            songs.customlist = songs.customlist + songs.luminousskylist
            print("All Luminous Sky Songs added to custom list")
            await ctx.channel.send("All Luminous Sky Songs added to custom list")

        elif packname == "vl":
            songs.customlist = songs.customlist + songs.viciouslabyrinthlist
            print("All Vicious Labyrinth Songs added to custom list")
            await ctx.channel.send("All Vicious Labyrinth Songs added to custom list")

        elif packname == "ec":
            songs.customlist = songs.customlist + songs.eternalcorelist
            print("All Eternal Core Songs added to custom list")
            await ctx.channel.send("All Eternal Core Songs added to custom list")

        elif packname == "ep":
            songs.customlist = songs.customlist + songs.ephemeralpagelist + songs.thejourneyonwardslist
            print("All Ephemeral Page Songs added to custom list")
            await ctx.channel.send("All Ephemeral Page Songs added to custom list")

        elif packname == "ep -append":
            songs.customlist = songs.customlist + songs.ephemeralpagelist
            print("All Ephemeral Page Songs added to custom list")
            await ctx.channel.send("All Ephemeral Page Songs added to custom list -append")

        elif packname == "tjo" or packname == "ep append":
            songs.customlist = songs.customlist + songs.thejourneyonwardslist
            print("All The Journey Onwards Songs added to custom list")
            await ctx.channel.send("All The Journey Onwards Songs added to custom list")

        elif packname == "eo":
            songs.customlist = songs.customlist + songs.esotericorderlist + songs.paletapestrylist
            print("All Esoteric Order Songs added to custom list")
            await ctx.channel.send("All Esoteric Order Songs added to custom list")

        elif packname == "eo -append":
            songs.customlist = songs.customlist + songs.esotericorderlist
            print("All Esoteric Order Songs added to custom list")
            await ctx.channel.send("All Esoteric Order Songs added to custom list -append")

        elif packname == "pt" or packname == "eo append":
            songs.customlist = songs.customlist + songs.paletapestrylist
            print("All Pale Tapestry Songs added to custom list")
            await ctx.channel.send("All Pale Tapestry Songs added to custom list")

        elif packname == "sr":
            songs.customlist = songs.customlist + songs.sunsetradiancelist
            print("All Sunset Radiance Songs added to custom list")
            await ctx.channel.send("All Sunset Radiance Songs added to custom list")

        elif packname == "ar":
            songs.customlist = songs.customlist + songs.absolutereasonlist
            print("All Absolute Reason Songs added to custom list")
            await ctx.channel.send("All Absolute Reason Songs added to custom list")

        elif packname == "be":
            songs.customlist = songs.customlist + songs.binaryenfoldlist
            print("All Binary Enfold Songs added to custom list")
            await ctx.channel.send("All Binary Enfold Songs added to custom list")

        elif packname == "av":
            songs.customlist = songs.customlist + songs.ambivalentvisionlist
            print("All Ambivalent Vision Songs added to custom list")
            await ctx.channel.send("All Ambivalent Vision Songs added to custom list")

        elif packname == "cs":
            songs.customlist = songs.customlist + songs.crimsonsolacelist
            print("All Crimson Solace Songs added to custom list")
            await ctx.channel.send("All Crimson Solace Songs added to custom list")

        elif packname == "dh":
            songs.customlist = songs.customlist + songs.dividedheartlist
            print("All Divided Heart Songs added to custom list")
            await ctx.channel.send("All Divided Heart Songs added to custom list")

        elif packname == "mai":
            songs.customlist = songs.customlist + songs.maimailist
            print("All maimai Songs added to custom list")
            await ctx.channel.send("All maimai Songs added to custom list")

        elif packname == "ong":
            songs.customlist = songs.customlist + songs.ongekilist
            print("All O.N.G.E.K.I. Songs added to custom list")
            await ctx.channel.send("All O.N.G.E.K.I. Songs added to custom list")

        elif packname == "chu":
            songs.customlist = songs.customlist + songs.chunithmlist + songs.chunithm2list
            print("All CHUNITHM Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Songs added to custom list")

        elif packname == "chu -append":
            songs.customlist = songs.customlist + songs.chunithmlist
            print("All CHUNITHM Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Songs added to custom list")

        elif packname == "chu2" or packname == "chu append":
            songs.customlist = songs.customlist + songs.chunithm2list
            print("All CHUNITHM Chapter 2 Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Chapter 2 Songs added to custom list")

        elif arg.startswith("gc", 8):
            songs.customlist = songs.customlist + songs.groovecoasterlist
            print("All Groove Coaster Songs added to custom list")
            await ctx.channel.send("All Groove Coaster Songs added to custom list")

        elif arg.startswith("ts", 8):
            songs.customlist = songs.customlist + songs.tonespherelist
            print("All Tone Sphere Songs added to custom list")
            await ctx.channel.send("All Tone Sphere Songs added to custom list")

        elif arg.startswith("lan", 8):
            songs.customlist = songs.customlist + songs.lanotalist
            print("All Lanota Songs added to custom list")
            await ctx.channel.send("All Lanota Songs added to custom list")

        elif arg.startswith("dnx", 8):
            songs.customlist = songs.customlist + songs.adversepreludelist
            print("All Dynamix Songs added to custom list")
            await ctx.channel.send("All Dynamix Songs added to custom list")

        else:
            await ctx.channel.send("Invalid pack or song name")
    else:
        print("Invalid argument for command $cuslist")
        await ctx.channel.send('Invalid argument for command $cuslist')