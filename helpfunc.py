async def helpfunc(ctx, arg):
    helpstr = ""
    if arg == "rand":
        await ctx.channel.send("``rand [pack]`` - Randomizes songs from a specific pack. The  ``free`` pack is pre-made for convenience for F2P players.")
    elif arg == "cuslist":
        await ctx.channel.send("``cuslist addpack [pack]`` - Add a pack to the custom list, you can add a pack more than once.\n``cuslist rm [int]`` - Remove a song from the list, song number is shown using ``cuslist view``. To remove duplicates, use ``dup`` instead of a number\n``cuslist view`` - View the custom list\n``cuslist reset`` - Reset the custom list to an empty list\n``cuslist filter [difficulty] [operator] [level]`` Filter only specific difficulties, supported operators are ``>``, ``<``, and ``=``. For ``X+`` difficulties, use ``X.7``. **Note the spaces between arguments**\n``save`` - Saves your current custom list and gives a hexadecimal code\n``load [code]`` - Loads a saved list from ``save`` command\n``searchsel [int]`` Add a song to the list, song number is showing using ``search [query]``.")
    elif arg == "combine":
        await ctx.channel.send("``combine [code1] and [code2]``- combines 2 list codes obtained from ``cuslist save`` to give a list of songs present in **both lists**\n``combine [code1] or [code2]``- combines 2 list codes obtained from ``cuslist save`` to give a list of songs present in **either list**")
    elif arg == "hard":
        await ctx.channel.send("``hard [shiny] [pure] [far] [lost]`` - A harder judge for shiny acc battling, uses RAVON's ratio of 5:3:1:0")
    elif arg == "exhard":
        await ctx.channel.send("``exhard [shiny] [pure] [far] [lost]`` - An even harder judge for shiny acc battling, pures are worth half of shinies, fars and below don't count")
    elif arg == "chuni":
        await ctx.channel.send("``chuni [shiny] [pure] [far] [lost]`` - An alternative scoring system based on CHUNITHM")
    elif arg == "pack":
        await ctx.channel.send("**Append packs are included in base packs, to exclude append, type ``-append`` after the base pack name**\n``all`` - All Songs\n``free`` - All Free Songs (Arcaea + World Extend)\n``ma`` - Memory Archive\n``arc`` - Arcaea\n``we`` - World Extend\n``bf`` - Black Fate\n``ap`` - Adverse Prelude\n``ls`` - Luminous Sky\n``vl`` - Vicious Labyrinth\n``ec`` - Eternal Core\n``sr`` - Sunset Radiance\n``ar`` - Absolute Reason\n``be`` - Binary Enfold\n``st`` - Shared Time\n``av`` - Ambivalent Vision\n``cs`` - Crimson Solace\n``ep`` - Ephemeral Page\n``tjo`` - The Journey Onwards\n``eo`` - Esoteric Order\n``pt`` - Pale Tapestry\n``los`` - Light of Salvation\n``dh`` - Divided Heart\n``mai`` - maimai\n``ong`` - O.N.G.E.K.I\n``chu`` - CHUNITHM\n``chu2`` - CHUNITHM Collab 2nd Chapter\n``gc`` - Groove Coaster\n``lan`` - Lanota\n``dnx`` - Dynamix\n``wac`` - WACCA\n``cus`` - Custom List")
    else:
        helpstr = "Current Arcbot Commands:```\n--------song list commands--------\nrand\ncuslist\ncombine\n\n--------alternative judge commands--------\nhard\nexhard\nchuni```"
        helpstr = helpstr + "For more information on each command, type ``$help [command]`` or for pack abbrieviations, type ``$help pack``"
        await ctx.channel.send(helpstr)
