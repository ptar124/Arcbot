import songs

async def searchfunc(ctx, query):
    songs.searchres = []
    for i in songs.dateorderedlist:
        if (i.gettitle().lower().find(query.lower()) > -1):
            songs.searchres.append(i)
            print("found" + query)
    searchview = "**Search Results:**\n```"

    j = 0
    while j < 10 and j < len(songs.searchres):
        searchview = searchview + str(j+1) + ". " + songs.searchres[j].gettitle() + "\n"
        j = j+1

    searchview = searchview + "```\nTo add song to custom list, use ``cuslist searchsel [int]``."
    await ctx.channel.send(searchview)