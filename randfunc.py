import random

async def randfunc(ctx, arg):
    global choice
    global picked

    global thislist
    global memoryarchivelist
    global arcaealist
    global worldextendlist
    global eternalcorelist
    global viciouslabyrinthlist
    global luminousskylist
    global adversepreludelist
    global blackfatelist
    global crimsonsolacelist
    global ambivalentvisionlist
    global binaryenfoldlist
    global absolutereasonlist
    global sunsetradiancelist
    global ephemeralpagelist
    global thejourneyonwardslist
    global esotericorderlist
    global paletapestrylist
    global songlist

    thislist = []

    if arg == "all":
        print("Random All")
        await ctx.channel.send('Random All Songs')
        thislist = songlist

    elif arg == "free":
        print("Random All Free Songs")
        await ctx.channel.send('Random All Free Songs')
        thislist = worldextendlist + arcaealist
    
    elif arg == "ma":
        print("Random Memory Archive Songs")
        await ctx.channel.send('Random All Memory Archive Songs')
        thislist = memoryarchivelist

    elif arg == "arc":
        print("Random Arcaea Songs")
        await ctx.channel.send('Random Arcaea Songs')
        thislist = arcaealist
        
    elif arg == "we":
        print("Random World Extend Songs")
        await ctx.channel.send('Random World Extend Songs')
        thislist = worldextendlist

    elif arg == "bf":
        print("Random Black Fate Songs")
        await ctx.channel.send('Random Black Fate Songs')
        thislist = blackfatelist

    elif arg == "ap":
        print("Random Adverse Prelude Songs")
        await ctx.channel.send('Random Adverse Prelude Songs')
        thislist = adversepreludelist

    elif arg == "ls":
        print("Random Luminous Sky Songs")
        await ctx.channel.send('Random Luminious Sky Songs')
        thislist = luminousskylist

    elif arg == "vl":
        print("Random Vicious Labyrinth Songs")
        await ctx.channel.send('Random Vicious Labyrinth Songs')
        thislist = viciouslabyrinthlist

    elif arg == "ec":
        print("Random Eternal Core Songs")
        await ctx.channel.send('Random Eternal Core Songs')
        thislist = eternalcorelist
    
    elif arg == "ep":
        print("Random Ephemeral Page Songs")
        await ctx.channel.send('Random Ephemeral Page Songs')
        thislist = ephemeralpagelist + thejourneyonwardslist
    
    elif arg == "ep -append":
        print("Random Ephemeral Page Songs")
        await ctx.channel.send('Random Ephemeral Page Songs -append')
        thislist = ephemeralpagelist

    elif arg == "tjo" or arg == "ep append":
        print("Random The Journey Onwards Songs")
        await ctx.channel.send('Random The Journey Onwards Songs')
        thislist = thejourneyonwardslist

    elif arg == "sr":
        print("Random Sunset Radiance Songs")
        await ctx.channel.send('Random Sunset Radiance Songs')
        thislist = sunsetradiancelist

    elif arg == "ar":
        print("Random Absolute Reason Songs")
        await ctx.channel.send('Random Absolute Reason Songs')
        thislist = absolutereasonlist
    
    elif arg == "be":
        print("Random Binary Enfold Songs")
        await ctx.channel.send('Random Binary Enfold Songs')
        thislist = binaryenfoldlist

    elif arg == "av":
        print("Radom Ambivalent Vision Songs")
        await ctx.channel.send('Random Abivalent Vision Songs')
        thislist = ambivalentvisionlist

    elif arg == "cs":
        print("Ramdom Crimson Solace Songs")
        await ctx.channel.send('Random Crimson Solace Songs')
        thislist = crimsonsolacelist

    elif arg == "eo":
        print("Ramdom Esoteric Order Songs")
        await ctx.channel.send('Random Esoteric Order Songs')
        thislist = esotericorderlist + paletapestrylist

    elif arg == "eo -append":
        print("Ramdom Esoteric Order Songs")
        await ctx.channel.send('Random Esoteric Order Songs -append')
        thislist = esotericorderlist

    elif arg == "pt" or arg == "eo append":
        print("Ramdom Pale Tapestry Songs")
        await ctx.channel.send('Random Pale Tapestry Songs')
        thislist = paletapestrylist

    elif arg == "mai":
        print("Random maimai Songs")
        await ctx.channel.send('Random maimai Songs')
        thislist = maimailist

    elif arg == "ong":
        print("Random O.N.G.E.K.I. Songs")
        await ctx.channel.send('Random O.N.G.E.K.I. Songs')
        thislist = ongekilist

    elif arg == "chu":
        print("Random CHUNITHM Songs")
        await ctx.channel.send('Random CHUNITHM Songs')
        thislist = chunithmlist + chunithm2list

    elif arg == "chu -append":
        print("Random CHUNITHM Songs")
        await ctx.channel.send('Random CHUNITHM Songs -append')
        thislist = chunithmlist
    
    elif arg == "chu2" or arg == "chu append":
        print("Random CHUNITHM Chapter 2 Songs")
        await ctx.channel.send('Random CHUNITHM Chapter 2 Songs')
        thislist = chunithm2list 

    elif arg == "gc":
        print("Random Groove Coaster Songs")
        await ctx.channel.send('Random Groove Coaster Songs')
        thislist = groovecoasterlist

    elif arg == "ts":
        print("Random Tone Sphere Songs")
        await ctx.channel.send('Random Tone Sphere Songs')
        thislist = tonespherelist
    
    elif arg == "lan":
        print("Random Lanota Songs")
        await ctx.channel.send('Random Lanota Songs')
        thislist = lanotalist

    elif arg == "dnx":
        print("Random Dynamix Songs")
        await ctx.channel.send('Random Dynamix Songs')
        thislist = dynamixlist

    elif arg == "cus":
        print("Random Custom List Songs")
        await ctx.channel.send('Random Custom List Songs')
        thislist = customlist

    else:
        print("Invalid argument for command $rand")
        await ctx.channel.send('Invalid argument for command $rand')

    for x in range (3):
        choice[x] = random.randint(0,len(thislist)-1)
        if x > 0:
            while choice[x] == choice[x-1]:
                choice[x] = random.randint(0,len(thislist)-1)
        if x > 1:
            while choice[x] == choice[x-2] or choice[x] == choice[x-1]:
                choice[x] = random.randint(0,len(thislist)-1)
        picked[x] = thislist[choice[x]].gettitle()

    await ctx.channel.send(':one: ' + picked[0] + '\n:two: ' + picked[1] + '\n:three: ' + picked[2] + "\n \nThe -append command has been implemented, if it's not working as intended, ping ptar124.")