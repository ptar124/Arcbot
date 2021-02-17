import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import random

#bot = discord.Client()
bot = commands.Bot(command_prefix = "$")
class Song:
    title = ""
    pstdiff = 0
    prsdiff = 0
    ftrdiff = 0
    byddiff = 0
    def __init__(self, title, pstdiff, prsdiff, ftrdiff, byddiff):
        self.title = title
        self.pstdiff = pstdiff
        self.prsdiff = prsdiff
        self.ftrdiff = ftrdiff
        self.byddiff = byddiff
    def gettitle(songid):
        return songid.title
    def getpstdiff(songid):
        return songid.pstdiff
    def getpsrsdiff(songid):
        return songid.prsdiff
    def getftrdiff(songid):
        return songid.ftrdiff
    def getbyddiff(songid):
        return songid.byddiff

#Arcaea Pack
song1 = Song("Sayonara Hatsukoi", 1, 4, 7, 0)
song2 = Song("Fairytale", 1, 3, 7, 9)
song3 = Song("Vexaria", 2, 5, 7, 8)
song4 = Song("Rise", 2, 4, 7, 0)
song5 = Song("Lucifer", 3, 5, 8, 0)
song6 = Song("Snow White", 2, 5, 8, 0)
song7 = Song("Shades of Light in a Transcendent Realm", 3, 6, 8, 0)
song8 = Song("Babaroque", 3, 6, 8, 0)
song9 = Song("Lost Civilisation", 4, 7, 9, 0)
song10 = Song("GOODTEK (Arcaea Edit)", 4, 6, 9, 9.7)
song11 = Song("qualia -ideaesthesia-", 4, 7, 9, 0)
song20 = Song("Dement ~after legend~", 3, 6, 7, 9.7)
song21 = Song("Dandelion", 2, 6, 8, 0)
song22 = Song("Infinity Heaven", 1, 5, 7, 9)
song23 = Song("Anökumene", 2, 6, 9, 0)
song24 = Song("Brand new world", 2, 4, 7, 0)
song30 = Song("Chronostasis", 3, 7, 9, 0)
song31 = Song("Kanagawa Cyber Culvert", 1, 5, 9, 0)
song35 = Song("Clotho and the stargazer", 2, 5, 7, 0)
song41 = Song("Ignotus", 3, 6, 9, 0)
song43 = Song("Harutopia -Utopia of Spring-", 1, 4, 8, 0)
song50 = Song("Rabbit in the Black Room", 2, 5, 8, 0)
song52 = Song("One Last Drive", 2, 5, 8, 0)
song53 = Song("Dreamin’ Attraction!!", 4, 7, 9, 0)
song54 = Song("Red and Blue", 4, 7, 9, 0)
song63 = Song("Reinvent", 2, 6, 8, 0)
song64 = Song("Syro", 3, 6, 9, 0)
song71 = Song("Blaster", 4, 7, 9, 0)
song79 = Song("Cybernecia Cartharsis", 4, 7, 9, 0)
song81 = Song("inkar-usi", 2, 4, 7, 0)
song83 = Song("Suomi", 2, 5, 7, 0)
song84 = Song("Bookmaker (2D Version)", 4, 6, 8, 0)
song85 = Song("Illegal Paradise", 2, 7, 9, 0)
song92 = Song("Nhelv", 3, 6, 9.7, 0)
song95 = Song("LunarOrbit -believe in the Espebranch road-", 3, 6, 9, 0)
song96 = Song("Purgatorium", 2, 6, 8, 9)
song103 = Song("Rugie", 3, 6, 9, 0)
song114 = Song("Grimheart", 2, 5, 8, 0)
song115 = Song("ReviXy", 3, 6, 9, 0)
song121 = Song("VECTOЯ", 3, 7, 9, 0)
song122 = Song("Supernova", 3, 6, 9.7, 0)
song138 = Song("Diode", 2, 5, 8, 0)
song139 = Song("FREEF4LL", 4, 7, 8, 0)
song141 = Song("Monochrome Princess", 4, 7, 9, 0)
song143 = Song("Senkyou", 3, 5, 8, 0)
song151 = Song("world.execute(me);", 3, 5, 8, 0)
song153 = Song("Oblivia", 3, 5, 8, 0)

#WE Pack
song163 = Song("Vivid Theory", 2, 5, 8, 0)
song164 = Song("1F√", 2, 6, 8, 0)
song165 = Song("Gekka (Short Version)", 4, 6, 8, 0)
song166 = Song("Give Me a Nightmare", 3, 5, 9, 0)
song167 = Song("Black Lotus", 3, 6, 9.7, 0)
song169 = Song("Faint Light (Arcaea Edit)", 3, 6, 9, 0)
song179 = Song("CROSS†OVER", 4, 6, 9, 0)
song180 = Song("Lapis", 2, 6, 9, 0)
song188 = Song("Purple Verse", 4, 7, 9, 0)
song204 = Song("Glow", 4, 7, 9, 0)
song205 = Song("enchanted love", 2, 4, 8, 0)
song206 = Song ("Bamboo", 3, 6, 9.7, 0)

#MA Pack
song32 = Song("DataErr0r", 3, 7, 9, 0)
song33 = Song("CROSS†SOUL", 4, 7, 9, 0)
song34 = Song("Your voice so... [feat. Such]", 3, 6, 9, 0)
song42 = Song("Impure Bird", 2, 5, 9, 0)
song49 = Song("Auxesia", 3, 6, 9, 0)
song51 = Song("Modelista", 3, 7, 10, 0)
song61 = Song("Surrender", 3, 6, 8, 0)
song62 = Song("Yosakura Fubuki", 4, 7, 9, 0)
song70 = Song("Metallic Punisher", 3, 7, 10, 0)
song77 = Song("carmine:scythe", 4, 7, 9, 0)
song78 = Song("γuarδina", 4, 7, 10, 0)
song80 = Song("Be There", 4, 7, 9, 0)
song82 = Song("Call My Name [feat. Yukacco]", 3, 6, 8, 0)
song93 = Song("dropdead", 1, 9, 8, 0)
song94 = Song("Fallensquare", 3, 7, 9, 0)
song97 = Song("Alexandrite", 4, 7, 10, 0)
song104 = Song("Astral tale", 4, 7, 9, 0)
song105 = Song("Phantasia", 4, 5, 9, 0)
song106 = Song("Empire of Winter", 3, 6, 9, 0)
song112 = Song("Libertas", 3, 5, 9, 0)
song123 = Song("Dot to Dot [feat. shully]", 3, 6, 8, 0)
song127 = Song("Dreadnought", 4, 7, 9.7, 0)
song137 = Song("Mirzam", 4, 7, 10, 0)
song142 = Song("Heavenly caress", 3, 7, 9.7, 0)
song144 = Song("Filament", 4, 7, 9.7, 0)
song145 = Song("Avant Raze", 3, 6, 9, 0)
song146 = Song("BATTLE NO. 1", 3, 6, 9.7, 0)
song147 = Song("La’qryma of the Wasteland", 3, 6, 9, 0)
song148 = Song("Einherjar Joker", 4, 7, 9.7, 0)
song149 = Song("IZANA", 5, 8, 10, 0)
song150 = Song("SAIKYO STRONGER", 5, 9, 11, 0)
song154 = Song("amygdata", 4, 7, 9, 0)
song168 = Song("Altale", 2, 5, 9.7, 0)
song170 = Song("Feels so Right [feat. Renko]", 3, 6, 9, 0)
song171 = Song("Scarlet Cage", 4, 7, 9.7, 0)
song172 = Song("Teriqma", 3, 6, 9, 0)
song173 = Song("MAHOROBA", 3, 6, 9, 0)
song174 = Song("BADTEK", 4, 7, 9.7, 0)
song175 = Song("Malicious Mischance", 4, 7, 10, 0)
song177 = Song("BUCHiGiRE Berserker", 5, 8, 10.7, 0)
song178 = Song("Galaxy Friends", 3, 6, 9.7, 0)
song181 = Song("Xeraphinite", 3, 7, 9.7, 0)
song182 = Song("Xanatos", 4, 7, 10, 0)
song203 = Song("AttraqtiA", 4, 7, 10, 0)

#EC Pack
song12 = Song("cry of viyella", 3, 6, 8, 0)
song13 = Song("I’ve heard it said", 3, 6, 8, 0)
song14 = Song("memoryfactory.lzh", 2, 5, 8, 0)
song15 = Song("Relentless", 4, 6, 8, 0)
song16 = Song("Lumia", 2, 5, 8, 9)
song17 = Song("Essence of Twilight", 4, 7, 9, 0)
song18 = Song("PRAGMATISM", 4, 8, 10, 0)
song19 = Song("Sheriruth", 5, 7, 10, 0)
song113 = Song("Solitary Dream", 4, 7, 8, 0)

#VL Pack
song55 = Song("Iconoclast", 4, 7, 9, 0)
song56 = Song("SOUNDWiTCH", 3, 6, 9.7, 0)
song57 = Song("trappola bewitching", 3, 6, 10, 0)
song58 = Song("conflict", 4, 7, 10, 0)
song59 = Song("Axium Crisis", 5, 8, 10.7, 0)
song60 = Song("Grievous Lady", 6, 9, 11, 0)

#LS Pack
song86 = Song("Maze No. 9", 3, 3, 8, 0)
song87 = Song("The Message", 3, 6, 9.7, 0)
song88 = Song("Sulfur", 4, 6, 9.7, 0)
song89 = Song("Halcyon", 5, 8, 10.7, 0)
song90 = Song("Ether Strike", 5, 8, 10, 0)
song91 = Song("Fracture Ray", 6, 9, 11, 0)

#AP Pack
song128 = Song("Particle Arts", 3, 6, 8, 0)
song129 = Song("Vindication", 4, 6, 9, 0)
song130 = Song("Heavensdoor", 4, 7, 9.7, 0)
song131 = Song("Ringed Genesis", 5, 8, 10.7, 0)
song152 = Song("BLRINK", 3, 7, 9.7, 0)

#BF Pack
song156 = Song("Equilibrium", 3, 6, 9, 0)
song157 = Song("Antagonism", 4, 7, 9.7, 0)
song158 = Song("Lost Desire", 4, 7, 9.7, 0)
song159 = Song("Dantalion", 5, 8, 10.7, 0)
song160 = Song("#1f1e33", 5, 9, 10.7, 0)
song161 = Song("Tempestissimo", 6, 9, 10, 11)
song162 = Song("Arcahv", 4, 7, 9.7, 0)

#CS Pack
song25 = Song("Paradise", 1, 4, 7, 0)
song26 = Song("Flashback", 2, 5, 8, 0)
song27 = Song("Flyburg and Endroll", 3, 6, 9, 0)
song28 = Song("Party Vinyl", 4, 7, 9, 0)
song29 = Song("Nirv lucE", 2, 7, 10, 0)
song140 = Song("GLORY : ROAD", 4, 7, 10, 0)

#AV Pack
song44 = Song("Blossoms", 1, 4, 7, 0)
song45 = Song("Romance Wars", 1, 4, 7, 0)
song46 = Song("Moonheart", 2, 5, 8, 9.7)
song47 = Song("Genesis", 2, 5, 8, 0)
song48 = Song("Lethaeus", 3, 6, 9.7, 0)
song155 = Song("corps-sans-organes", 4, 7, 10, 0)

#BE Pack
song72 = Song("next to you", 4, 7, 8, 0)
song73 = Song("Silent Rush", 2, 5, 8, 0)
song74 = Song("Strongholds", 2, 5, 9, 0)
song75 = Song("Memory Forest", 3, 6, 9.7, 0)
song76 = Song("Singularity", 4, 7, 10.7, 0)

#AR Pack
song116 = Song("Antithese", 2, 5, 8, 0)
song117 = Song("Black Territory", 3, 7, 9.7, 0)
song118 = Song("Corruption", 3, 6, 9.7, 0)
song119 = Song("Vicious Heroism", 4, 7, 10, 0)
song120 = Song("Cyaegha", 5, 8, 10.7, 0)

#SR Pack
song132 = Song("Chelsea", 3, 6, 8, 0)
song133 = Song("AI[UE]OON", 3, 6, 9, 0)
song134 = Song("A Wandering Melody of Love", 3, 7, 9.7, 0)
song135 = Song("Tie me down gently", 3, 5, 8, 0)
song136 = Song("Valhalla:0", 4, 7, 10, 0)

#EP Pack
song183 = Song("Alice à la mode", 2, 6, 9, 0)
song184 = Song("Eccentric Tale", 2, 5, 8, 0)
song185 = Song("Alice’s Suitcase", 3, 6, 9, 0)
song186 = Song("Jump", 4, 6, 9, 0)
song187 = Song("Felis", 4, 7, 10, 0)
song189 = Song("Beside You", 2, 6, 8, 0)
song190 = Song("Heart Jackin’", 3, 5, 9.7, 0)
song191 = Song("To: Alice Liddell", 4, 7, 10, 0)

#DNX Pack
song36 = Song("Moonlight of Sand Castle", 1, 5, 7, 0)
song37 = Song("REconstruction", 2, 6, 8, 0)
song38 = Song("Evoltex (poppi’n mix)", 2, 7, 8, 0)
song39 = Song("Oracle", 3, 5, 9, 0)
song40 = Song("αterlβus", 4, 7, 10, 0)

#Lan Pack
song65 = Song("Dream goes on", 1, 5, 7, 0)
song66 = Song("Journey", 3, 6, 8, 0)
song67 = Song("Specta", 3, 6, 9, 0)
song68 = Song("Quon", 4, 6, 9.7, 0)
song69 = Song("cyanine", 4, 7, 10, 0)

#TS Pack
song98 = Song("Hikari", 2, 6, 8, 0)
song99 = Song("Hall of Mirrors", 3, 5, 8, 0)
song100 = Song("STAGER (ALL STAGE CLEAR)", 3, 6, 9, 0)
song101 = Song("Linear Accelerator", 2, 6, 9.7, 0)
song102 = Song("Tiferet", 4, 7, 10, 0)

#GC Pack
song107 = Song("MERLIN", 3, 5, 8, 0)
song108 = Song("DX Choseinou Full Metal Shojo", 3, 6, 9.7, 0)
song109 = Song("OMAKENO Stroke", 3, 6, 9, 0)
song110 = Song("Scarlet Lance", 4, 7, 10, 0)
song111 = Song("ouroboros ~twin stroke of the end~", 4, 7, 10.7, 0)
song176 = Song("Got hive of Ra", 3, 6, 9.7, 0)

#Chu Pack
song124 = Song("Garakuta Doll Play", 4, 6, 10, 0)
song125 = Song("Ikazuchi", 3, 7, 10, 0)
song126 = Song("World Vanquisher", 2, 5, 10.7, 0)
song200 = Song("Climax", 4, 7, 10, 0)
song201 = Song("Last Celebration", 3, 6, 10, 0)
song202 = Song("Misdeed -la bonté de Dieu et l’origine du mal-", 5, 8, 10.7, 0)

#Ong Pack
song192 = Song("Lazy Addiction", 2, 6, 9, 0)
song193 = Song("Dazzle hop", 3, 6, 9.7, 0)
song194 = Song("Viyella’s Tears", 4, 7, 10, 0)
song195 = Song("ω4", 3, 7, 10.7, 0)

#mai Pack
song196 = Song("April showers", 2, 5, 8, 0)
song197 = Song("7thSense", 3, 7, 9.7, 0)
song198 = Song("Oshama Scramble!", 3, 6, 10, 0)
song199 = Song("AMAZING MIGHTYYYY!!!!", 4, 7, 10.7, 0)

choice = [0, 0, 0]
picked = ["", "", ""]

memoryarchivelist = [song32, song33, song34, song42, song49, song51, song61, song62, song70, song77, song78, song80, song82, song93, song94, song97, song104, song105, song106, song112, song123, song127, song137, song142, song144, song145, song146, song147, song148, song149, song150, song154, song168, song170, song171, song172, song173, song174, song175, song177, song178, song181, song182, song203]

arcaealist = [song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song20, song21, song22, song23, song24, song30, song31, song35, song41, song43, song50, song52, song53, song54, song63, song64, song71, song79, song81, song83, song84, song85, song92, song95, song96, song103, song114, song115, song121, song122, song138, song139, song141, song143, song151, song153]

worldextendlist = [song163, song164, song165, song166, song167, song169, song179, song180, song188, song204, song205, song206]

blackfatelist = [song156, song157, song158, song159, song160, song161, song162]

adversepreludelist = [song128, song129, song130, song131, song152]

luminousskylist = [song86, song87, song88, song89, song90, song91]

viciouslabyrinthlist = [song55, song56, song57, song58, song59, song60]

eternalcorelist = [song12, song13, song14, song15, song16, song17, song18, song19, song113]

ephemeralpagelist = [song183, song184, song185, song186, song187, song189, song190, song191]

sunsetradiancelist = [song132, song133, song134, song135, song136]

absolutereasonlist = [song116, song117, song118, song119, song120]

binaryenfoldlist = [song72, song73, song74, song75, song76]

ambivalentvisionlist = [song44, song45, song46, song47, song48, song155]

crimsonsolacelist = [song25, song26, song27, song28, song29, song140]

maimailist = [song196, song197, song198, song199]

ongekilist = [song192, song193, song194, song195]

chunithmlist = [song124, song125, song126, song200, song201, song202]

groovecoasterlist = [song107, song108, song109, song110, song111, song176]

tonespherelist = [song98, song99, song100, song101, song102]

lanotalist = [song65, song66, song67, song68, song69]

dynamixlist = [song36, song37, song38, song39, song40]

songlist = memoryarchivelist + arcaealist + worldextendlist + blackfatelist + adversepreludelist + luminousskylist + viciouslabyrinthlist + eternalcorelist + ephemeralpagelist + sunsetradiancelist + absolutereasonlist + binaryenfoldlist + ambivalentvisionlist + crimsonsolacelist + maimailist + ongekilist + chunithmlist + groovecoasterlist + tonespherelist + lanotalist + dynamixlist

freelist = worldextendlist + arcaealist

customlist = []

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
    global customlist

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
        thislist = ephemeralpagelist

    elif arg == "sr":
        print("Random Sunset Radiance Songs")
        await ctx.channel.send('Random Sunset Radiance Songs')
        thislist = sunsetradiancelist

    elif arg == "ar":
        print("Random Absolute Reason Songs")
        await ctx.channel.send('Random Absolute ReasonSongs')
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
        thislist = chunithmlist

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

    await ctx.channel.send(':one: ' + picked[0] + '\n:two: ' + picked[1] + '\n:three: ' + picked[2] + '\n \n**Currently all append packs are included in their respective main packs**')

@bot.command()
async def cuslist(ctx, *, arg):
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

    elif arg == "view":
        customlistview = "**Current song list:** ```"
        for x in range(len(customlist)):
            customlistview = customlistview + str(x+1) + ". " + customlist[x].gettitle() + " \n"
        customlistview = customlistview + "``` To remove songs, use ``cuslist rm [song number]``"

        if len(customlistview) > 1999:
            await ctx.channel.send("Your song list exceeds Discord's character limit and cannot be viewed")           
        elif customlist == []:
            await ctx.channel.send("You can't view an empty list!")
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
                        if customlist[x].getpstdiff() > diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getpstdiff() < diffarg:
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
                        if customlist[x].getprsdiff() > diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getprsdiff() < diffarg:
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
                        if customlist[x].getftrdiff() > diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getftrdiff() < diffarg:
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
                        if customlist[x].getbyddiff() > diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
                elif oparg == ">":
                    x = 0
                    while x < len(customlist):
                        if customlist[x].getbyddiff() < diffarg:
                            customlist.pop(x)
                        else:
                            x = x+1
            else:
                await ctx.channel.send("Invalid difficulty, level, or operation")

            await ctx.channel.send("Applied Filter: " + arg[7:10] + " " + oparg + " " + str(diffarg) + "\n **This feature is still experimental, please double check the list**")

        else:
            await ctx.channel.send("Invalid difficulty, level, or operation")


    elif arg.startswith("addpack"):
        if arg.startswith("all", 8):
            customlist = customlist + songlist
            print("All Songs added to custom list")
            await ctx.channel.send("All Songs added to custom list")

        elif arg.startswith("free", 8):
            customlist = customlist + freelist
            print("All Free Songs added to custom list")
            await ctx.channel.send("All Free Songs added to custom list")

        elif arg.endswith("ma", 8):
            customlist = customlist + memoryarchivelist
            print("All Memory Archive Songs added to custom list")
            await ctx.channel.send("All Memory Archive Songs added to custom list")

        elif arg.startswith("arc", 8):
            customlist = customlist + arcaealist
            print("All Arcaea Pack Songs added to custom list")
            await ctx.channel.send("All Arcaea Pack Songs added to custom list")

        elif arg.startswith("we", 8):
            customlist = customlist + worldextendlist
            print("All World Extend Songs added to custom list")
            await ctx.channel.send("All World Extend Songs added to custom list")

        elif arg.startswith("bf", 8):
            customlist = customlist + blackfatelist
            print("All Black Fate Songs added to custom list")
            await ctx.channel.send("All Black Fate Songs added to custom list")

        elif arg.startswith("ap", 8):
            customlist = customlist + adversepreludelist
            print("All Adverse Prelude Songs added to custom list")
            await ctx.channel.send("All Adverse Prelude Songs added to custom list")

        elif arg.startswith("ls", 8):
            customlist = customlist + luminousskylist
            print("All Luminous Sky Songs added to custom list")
            await ctx.channel.send("All Luminous Sky Songs added to custom list")

        elif arg.startswith("vl", 8):
            customlist = customlist + viciouslabyrinthlist
            print("All Vicious Labyrinth Songs added to custom list")
            await ctx.channel.send("All Vicious Labyrinth Songs added to custom list")

        elif arg.startswith("ec", 8):
            customlist = customlist + eternalcorelist
            print("All Eternal Core Songs added to custom list")
            await ctx.channel.send("All Eternal Core Songs added to custom list")

        elif arg.startswith("ep", 8):
            customlist = customlist + ephemeralpagelist
            print("All Ephemeral Page Songs added to custom list")
            await ctx.channel.send("All Ephemeral Page Songs added to custom list")

        elif arg.startswith("sr", 8):
            customlist = customlist + sunsetradiancelist
            print("All Sunset Radiance Songs added to custom list")
            await ctx.channel.send("All Sunset Radiance Songs added to custom list")

        elif arg.startswith("ar", 8):
            customlist = customlist + absolutereasonlist
            print("All Absolute Reason Songs added to custom list")
            await ctx.channel.send("All Absolute Reason Songs added to custom list")

        elif arg.startswith("be", 8):
            customlist = customlist + binaryenfoldlist
            print("All Binary Enfold Songs added to custom list")
            await ctx.channel.send("All Binary Enfold Songs added to custom list")

        elif arg.startswith("av", 8):
            customlist = customlist + ambivalentvisionlist
            print("All Ambivalent Vision Songs added to custom list")
            await ctx.channel.send("All Ambivalent Vision Songs added to custom list")

        elif arg.startswith("cs", 8):
            customlist = customlist + crimsonsolacelist
            print("All Crimsone Solace Songs added to custom list")
            await ctx.channel.send("All Crimson Solace Songs added to custom list")

        elif arg.startswith("mai", 8):
            customlist = customlist + maimailist
            print("All maimai Songs added to custom list")
            await ctx.channel.send("All maimai Songs added to custom list")

        elif arg.startswith("ong", 8):
            customlist = customlist + ongekilist
            print("All O.N.G.E.K.I. Songs added to custom list")
            await ctx.channel.send("All O.N.G.E.K.I. Songs added to custom list")

        elif arg.startswith("chu", 8):
            customlist = customlist + chunithmlist
            print("All CHUNITHM Songs added to custom list")
            await ctx.channel.send("All CHUNITHM Songs added to custom list")

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

        elif arg.startswith("dyn", 8):
            customlist = customlist + adversepreludelist
            print("All Dynamix Songs added to custom list")
            await ctx.channel.send("All Dynamix Songs added to custom list")

        else:
            await ctx.channel.send("Invalid pack or song name")
    else:
        print("Invalid argument for command $cuslist")
        await ctx.channel.send('Invalid argument for command $cuslist')

keep_alive()
bot.run(os.getenv('TOKEN'))