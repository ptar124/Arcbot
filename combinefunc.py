async def combinefunc(ctx, code1, op, code2):
    hexinput1 = int(code1, 16)
    hexinput2 = int(code2, 16)
    bitwiseop = op

    bininput1 = bin(hexinput1).replace("0b", "")
    bininput2 = bin(hexinput2).replace("0b", "")

    zeroesneeded = 256 - len(bininput1)
    zeroesstring = ""
    for x in range (zeroesneeded):
        zeroesstring = zeroesstring + "0"
    
    binstring1 = zeroesstring + bininput1
    decstring1 = int(binstring1, 2)
    print("hex1: " + code1 )
    print("bin1: " + binstring1)

    zeroesneeded = 256 - len(bininput2)
    zeroesstring = ""
    for x in range (zeroesneeded):
         zeroesstring = zeroesstring + "0"

    binstring2 = zeroesstring + bininput2
    decstring2 = int(binstring2, 2)
    print("hex2: " + code2 )
    print("bin2: " + binstring2)

    if bitwiseop == "and":
        newdec = decstring1 & decstring2
    elif bitwiseop == "or":
        newdec = decstring1 | decstring2

    newbin = bin(newdec).replace("0b", "")

    zeroesneeded = 256 - len(newbin)
    zeroesstring = ""
    for x in range (zeroesneeded):
         zeroesstring = zeroesstring + "0"

    newbin = zeroesstring + newbin
    newhex = hex(int("0b" + newbin, 2))
    print("bin out: " + newbin)
    print("hex out: " + newhex)

    await ctx.channel.send("The combined code (bitwise **" + bitwiseop + "** operation) of the two lists is\n``" + newhex + "``")