import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import random

#bot = discord.Client()
bot = commands.Bot(command_prefix = "$")

choice = [0, 0, 0]
picked = ["", "", ""]

memoryarchivelist = ["DataErr0r", "CROSS†SOUL", "Your voice so... feat. Such", "Impure Bird", "Auxesia", "Modelista", "Surrender", "Yosakura Fubuki", "Metallic Punisher", "carmine:scythe", "γuarδina", "Be There", "Call My Name feat. Yukacco", "dropdead", "Fallensquare", "Alexandrite", "Astral tale", "Phantasia", "Empire of Winter", "Libertas", "Dot to Dot feat. shully", "Dreadnought", "Mirzam", "Heavenly caress", "Filament", "Avant Raze", "BATTLE NO.1", "La'qryma of the Wasteland", "Einherjar Joker", "IZANA", "SAIKYO STRONGER", "amygdata", "Altale", "Scarlet Cage", "Feels So Right feat. Renko", "Teriqma", "MAHOROBA", "BADTEK", "Malicious Mischance", "BUCHiGiRE Berserker", "Galaxy Friends", "Xeraphinite", "Xanatos", "AttraqtiA"]

arcaealist = ["Sayonara Hatsukoi", "Fairytale", "Vexaria", "Rise", "Lucifer", "Snow White", "Shades of Light in a Transcendent Realm", "Babaroque", "Lost Civilization", "GOODTEK (Arcaea Edit)", "qualia -ideaesthesia-", "Dement ~after legend~", "Dandelion", "Infinity Heaven", "Anökumene", "Brand new world", "Chronostasis", "Kanagawa Cyber Culvert", "Clotho and the stargazer", "Ignotus", "Harutopia ~Utopia of Spring~", "Rabbit In The Black Room", "One Last Drive", "Dreamin' Attraction!!", "Red and Blue", "Reinvent", "Syro", "Blaster", "Cybernecia Catharsis", "inkar-usi", "Suomi", "Bookmaker (2D Version)", "Illegal Paradise", "Nhelv", "LunarOrbit -believe in the Espebranch road-", "Purgatorium", "Rugie", "Grimheart", "ReviXy", "VECTOЯ", "SUPERNOVA", "Diode", "FREEF4LL", "Monochrome Princess", "Senkyou", "world.execute(me);", "Oblivia"]

worldextendlist = ["Vivid Theory", "1F√", "Gekka (Short Version)", "Give Me A Nightmare", "Black Lotus", "Faint Light (Arcaea Edit)", "CROSS†OVER", "Lapis", "Purple Verse"]

blackfatelist = ["Equilibrium", "Antagonism", "Lost Desire", "Dantalion", "#1f1e33", "Tempestissimo", "Arcahv"]

adversepreludelist = ["Particle Arts", "Vindication", "Heavensdoor", "Ringed Genesis", "BLRINK"]

luminousskylist = ["Maze No.9", "The Message", "Sulfur", "Halcyon", "Ether Strike", "Fracture Ray"]

viciouslabyrinthlist = ["Iconoclast", "SOUNDWiTCH", "trappola bewitching", "conflict", "Axium Crisis", "Grievous Lady"]

eternalcorelist = ["cry of viyella", "I've heard it said", "memoryfactory.lzh", "Relentless", "Lumia", "Essence of Twilight", "PRAGMATISM", "Sheriruth", "Solitary Dream"]

ephemeralpagelist = ["Alice à la mode", "Eccentric Tale", "Alice's Suitcase", "Jump", "Felis", "Beside You", "Heart Jackin'", "To: Alice Liddell"]

sunsetradiancelist = ["Chelsea", "AI[UE]OON", "A Wandering Melody of Love", "Tie me down gently", "Valhalla:0"]

absolutereasonlist = ["Antithese", "Black Territory", "Corruption", "Vicious Heroism", "Cyaegha"]

binaryenfoldlist = ["next to you", "Silent Rush", "Strongholds", "Memory Forest", "Singularity"]

ambivalentvisionlist = ["Blossoms", "Romance Wars", "Moonheart", "Genesis", "Lethaeus", "corps-sans-organes"]

crimsonsolacelist = ["Paradise", "Flashback", "Flyburg and Endroll", "Party Vinyl", "Nirv lucE", "GLORY：ROAD"]

maimailist = ["April showers", "7thSense", "Oshama Scramble!", "AMAZING MIGHTYYYY!!!!"]

ongekilist = ["Lazy Addiction", "Dazzle hop", "Viyella's Tears", "ω4"]

chunithmlist = ["Garakuta Doll Play", "Ikazuchi", "World Vanquisher",  "Climax", "Last Celebration", "Misdeed -la bonté de Dieu et l'origine du mal-"]

groovecoasterlist = ["MERLIN", "DX Choseinou Full Metal Shojo", "OMAKENO Stroke", "Scarlet Lance", "ouroboros -twin stroke of the end-", "Got hive of Ra"]

tonespherelist = ["Hikari", "Hall of Mirrors", "STAGER (ALL STAGE CLEAR)", "Linear Accelerator", "Tiferet"]

lanotalist = ["Dream goes on", "Journey", "Specta", "Quon", "cyanine"]

dynamixlist = ["Moonlight of Sand Castle", "REconstruction", "Evoltex (poppi'n mix)", "Oracle", "αterlβus"]

songlist = memoryarchivelist + arcaealist + worldextendlist + blackfatelist + adversepreludelist + luminousskylist + viciouslabyrinthlist + eternalcorelist + ephemeralpagelist + sunsetradiancelist + absolutereasonlist + binaryenfoldlist + ambivalentvisionlist + crimsonsolacelist + maimailist + ongekilist + chunithmlist + groovecoasterlist + tonespherelist + lanotalist + dynamixlist

freelist = worldextendlist + arcaealist

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def rand(ctx, arg):
 
    global rng
    global choice
    global picked

    global memoryarchivelist
    global arcaealist
    global worldextendlist
    global blackfatelist
    global adversepreludelist
    global luminousskylist
    global viciouslabyrinthlist
    global eternalcorelist
    global ephemeralpagelist
    global sunsetradiancelist
    global absolutereasonlist
    global binaryenfoldlist
    global ambivalentvisionlist
    global crimsonsolacelist
    global maimailist
    global ongekilist
    global chunithmlist
    global groovecoasterlist
    global tonespherelist
    global lanotalist
    global dynamixlist
    global songlist
    global freelist

    thislist = []

    if arg == "all":
        print("Random All")
        await ctx.channel.send('Random All Songs')
        thislist = songlist

    if arg == "free":
        print("Random All Free Songs")
        await ctx.channel.send('Random All Free Songs')
        thislist = worldextendlist + arcaealist
    
    if arg == "ma":
        print("Random Memory Archive Songs")
        await ctx.channel.send('Random All Memory Archive Songs')
        thislist = memoryarchivelist

    if arg == "arc":
        print("Random Arcaea Songs")
        await ctx.channel.send('Random Arcaea Songs')
        thislist = arcaealist
        
    if arg == "we":
        print("Random World Extend Songs")
        await ctx.channel.send('Random World Extend Songs')
        thislist = worldextendlist

    if arg == "bf":
        print("Random Black Fate Songs")
        await ctx.channel.send('Random Black Fate Songs')
        thislist = blackfatelist

    if arg == "ap":
        print("Random Adverse Prelude Songs")
        await ctx.channel.send('Random Adverse Prelude Songs')
        thislist = adversepreludelist

    if arg == "ls":
        print("Random Luminous Sky Songs")
        await ctx.channel.send('Random Luminious Sky Songs')
        thislist = luminousskylist

    if arg == "vl":
        print("Random Vicious Labyrinth Songs")
        await ctx.channel.send('Random Vicious Labyrinth Songs')
        thislist = viciouslabyrinthlist

    if arg == "ec":
        print("Random Eternal Core Songs")
        await ctx.channel.send('Random Eternal Core Songs')
        thislist = eternalcorelist
    
    if arg == "ep":
        print("Random Ephemeral Page Songs")
        await ctx.channel.send('Random Ephemeral Page Songs')
        thislist = ephemeralpagelist

    if arg == "sr":
        print("Random Sunset Radiance Songs")
        await ctx.channel.send('Random Sunset Radiance Songs')
        thislist = sunsetradiancelist

    if arg == "ar":
        print("Random Absolute Reason Songs")
        await ctx.channel.send('Random Absolute ReasonSongs')
        thislist = absolutereasonlist
    
    if arg == "be":
        print("Random Binary Enfold Songs")
        await ctx.channel.send('Random Binary Enfold Songs')
        thislist = binaryenfoldlist

    if arg == "av":
        print("Radom Ambivalent Vision Songs")
        await ctx.channel.send('Random Abivalent Vision Songs')
        thislist = ambivalentvisionlist

    if arg == "cs":
        print("Ramdom Crimson Solace Songs")
        await ctx.channel.send('Random Crimson Solace Songs')
        thislist = crimsonsolacelist

    if arg == "mai":
        print("Random maimai Songs")
        await ctx.channel.send('Random maimai Songs')
        thislist = maimailist

    if arg == "ong":
        print("Random O.N.G.E.K.I. Songs")
        await ctx.channel.send('Random O.N.G.E.K.I. Songs')
        thislist = ongekilist

    if arg == "chu":
        print("Random CHUNITHM Songs")
        await ctx.channel.send('Random CHUNITHM Songs')
        thislist = chunithmlist

    if arg == "gc":
        print("Random Groove Coaster Songs")
        await ctx.channel.send('Random Groove Coaster Songs')
        thislist = groovecoasterlist

    if arg == "ts":
        print("Random Tone Sphere Songs")
        await ctx.channel.send('Random Tone Sphere Songs')
        thislist = tonespherelist
    
    if arg == "lan":
        print("Random Lanota Songs")
        await ctx.channel.send('Random Lanota Songs')
        thislist = lanotalist

    if arg == "dnx":
        print("Random Dynamix Songs")
        await ctx.channel.send('Random Dynamix Songs')
        thislist = dynamixlist

    for x in range (3):
        choice[x] = random.randint(0,len(thislist)-1)
        if x > 0:
            while choice[x] == choice[x-1]:
                choice[x] = random.randint(0,len(thislist)-1)
        if x > 1:
            while choice[x] == choice[x-2] or choice[x] == choice[x-1]:
                choice[x] = random.randint(0,len(thislist)-1)
        picked[x] = thislist[choice[x]]

    await ctx.channel.send(':one: ' + picked[0] + '\n:two: ' + picked[1] + '\n:three: ' + picked[2] + '\n \n**Currently all append packs are included in their respective main packs**')

keep_alive()
bot.run(os.getenv('TOKEN'))