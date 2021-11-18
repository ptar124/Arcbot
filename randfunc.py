import random
import songs

async def randfunc(ctx, arg):

    thislist = []

    if arg == "all":
        print("Random All")
        await ctx.channel.send('Random All Songs')
        thislist = songs.dateorderedlist

    elif arg == "free":
        print("Random All Free Songs")
        await ctx.channel.send('Random All Free Songs')
        thislist = songs.worldextendlist + songs.arcaealist
    
    elif arg == "ma":
        print("Random Memory Archive Songs")
        await ctx.channel.send('Random All Memory Archive Songs')
        thislist = songs.memoryarchivelist

    elif arg == "arc":
        print("Random Arcaea Songs")
        await ctx.channel.send('Random Arcaea Songs')
        thislist = songs.arcaealist
        
    elif arg == "we":
        print("Random World Extend Songs")
        await ctx.channel.send('Random World Extend Songs')
        thislist = songs.worldextendlist

    elif arg == "bf":
        print("Random Black Fate Songs")
        await ctx.channel.send('Random Black Fate Songs')
        thislist = songs.blackfatelist

    elif arg == "ap":
        print("Random Adverse Prelude Songs")
        await ctx.channel.send('Random Adverse Prelude Songs')
        thislist = songs.adversepreludelist

    elif arg == "ls":
        print("Random Luminous Sky Songs")
        await ctx.channel.send('Random Luminious Sky Songs')
        thislist = songs.luminousskylist

    elif arg == "vl":
        print("Random Vicious Labyrinth Songs")
        await ctx.channel.send('Random Vicious Labyrinth Songs')
        thislist = songs.viciouslabyrinthlist

    elif arg == "ec":
        print("Random Eternal Core Songs")
        await ctx.channel.send('Random Eternal Core Songs')
        thislist = songs.eternalcorelist
    
    elif arg == "ep":
        print("Random Ephemeral Page Songs")
        await ctx.channel.send('Random Ephemeral Page Songs')
        thislist = songs.ephemeralpagelist + songs.thejourneyonwardslist
    
    elif arg == "ep -append":
        print("Random Ephemeral Page Songs")
        await ctx.channel.send('Random Ephemeral Page Songs -append')
        thislist = songs.ephemeralpagelist

    elif arg == "tjo" or arg == "ep append":
        print("Random The Journey Onwards Songs")
        await ctx.channel.send('Random The Journey Onwards Songs')
        thislist = songs.thejourneyonwardslist

    elif arg == "sr":
        print("Random Sunset Radiance Songs")
        await ctx.channel.send('Random Sunset Radiance Songs')
        thislist = songs.sunsetradiancelist

    elif arg == "ar":
        print("Random Absolute Reason Songs")
        await ctx.channel.send('Random Absolute Reason Songs')
        thislist = songs.absolutereasonlist
    
    elif arg == "be":
        print("Random Binary Enfold Songs")
        await ctx.channel.send('Random Binary Enfold Songs')
        thislist = songs.binaryenfoldlist + songs.sharedtimelist

    elif arg == "be -append":
        print("Random Binary Enfold Songs")
        await ctx.channel.send('Random Binary Enfold Songs -append')
        thislist = songs.binaryenfoldlist
    
    elif arg == "st" or arg == "be append":
        print("Random Shared Time Songs")
        await ctx.channel.send('Random Shared Time Songs')
        thislist = songs.sharedtimelist

    elif arg == "av":
        print("Radom Ambivalent Vision Songs")
        await ctx.channel.send('Random Abivalent Vision Songs')
        thislist = songs.ambivalentvisionlist

    elif arg == "cs":
        print("Ramdom Crimson Solace Songs")
        await ctx.channel.send('Random Crimson Solace Songs')
        thislist = songs.crimsonsolacelist

    elif arg == "eo":
        print("Ramdom Esoteric Order Songs")
        await ctx.channel.send('Random Esoteric Order Songs')
        thislist = songs.esotericorderlist + songs.paletapestrylist + songs.lightofsalvationlist

    elif arg == "eo -append":
        print("Ramdom Esoteric Order Songs")
        await ctx.channel.send('Random Esoteric Order Songs -append')
        thislist = songs.esotericorderlist

    elif arg == "pt" or arg == "eo append":
        print("Ramdom Pale Tapestry Songs")
        await ctx.channel.send('Random Pale Tapestry Songs')
        thislist = songs.paletapestrylist

    elif arg == "los" or arg == "eo append 2":
        print("Ramdom Light of Salvation Songs")
        await ctx.channel.send('Random Light of Salvation Songs')
        thislist = songs.paletapestrylist

    elif arg == "dh":
        print("Ramdom Divided Heart Songs")
        await ctx.channel.send('Random Divided Heart Songs')
        thislist = songs.dividedheartlist

    elif arg == "mai":
        print("Random maimai Songs")
        await ctx.channel.send('Random maimai Songs')
        thislist = songs.maimailist

    elif arg == "ong":
        print("Random O.N.G.E.K.I. Songs")
        await ctx.channel.send('Random O.N.G.E.K.I. Songs')
        thislist = songs.ongekilist

    elif arg == "chu":
        print("Random CHUNITHM Songs")
        await ctx.channel.send('Random CHUNITHM Songs')
        thislist = songs.chunithmlist + songs.chunithm2list

    elif arg == "chu -append":
        print("Random CHUNITHM Songs")
        await ctx.channel.send('Random CHUNITHM Songs -append')
        thislist = songs.chunithmlist
    
    elif arg == "chu2" or arg == "chu append":
        print("Random CHUNITHM Chapter 2 Songs")
        await ctx.channel.send('Random CHUNITHM Chapter 2 Songs')
        thislist = songs.chunithm2list 

    elif arg == "gc":
        print("Random Groove Coaster Songs")
        await ctx.channel.send('Random Groove Coaster Songs')
        thislist = songs.groovecoasterlist

    elif arg == "ts":
        print("Random Tone Sphere Songs")
        await ctx.channel.send('Random Tone Sphere Songs')
        thislist = songs.tonespherelist
    
    elif arg == "lan":
        print("Random Lanota Songs")
        await ctx.channel.send('Random Lanota Songs')
        thislist = songs.lanotalist

    elif arg == "dnx":
        print("Random Dynamix Songs")
        await ctx.channel.send('Random Dynamix Songs')
        thislist = songs.dynamixlist

    elif arg == "wac":
        print("Random WACCA Songs")
        await ctx.channel.send('Random WACCA Songs')
        thislist = songs.waccalist

    elif arg == "cus":
        print("Random Custom List Songs")
        await ctx.channel.send('Random Custom List Songs')
        thislist = songs.customlist

    else:
        print("Invalid argument for command $rand")
        await ctx.channel.send('Invalid argument for command $rand')

    for x in range (3):
        songs.choice[x] = random.randint(0,len(thislist)-1)
        if x > 0:
            while songs.choice[x] == songs.choice[x-1]:
                songs.choice[x] = random.randint(0,len(thislist)-1)
        if x > 1:
            while songs.choice[x] == songs.choice[x-2] or songs.choice[x] == songs.choice[x-1]:
                songs.choice[x] = random.randint(0,len(thislist)-1)
        songs.picked[x] = thislist[songs.choice[x]].gettitle()

    message = await ctx.channel.send(':one: ' + songs.picked[0] + '\n:two: ' + songs.picked[1] + '\n:three: ' + songs.picked[2] + "\n \nBot dev help wanted, ping ptar124 if you have programming experience and want to contribute!\nCustom list save and load now implemented, go make your own personal list!")
    
    emojilist = ['1️⃣', '2️⃣', '3️⃣']
    for x in range (3):
        await message.add_reaction(emojilist[x])
