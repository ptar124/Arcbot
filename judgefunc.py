async def hardfunc(ctx, s, p, f, l):    
    shiny = float(s)
    pure = float(p) - float(s)
    far = float(f)
    lost = float(l)
    ncount = shiny + pure + far + lost
    sscore = 10000000/ncount
    pscore = sscore*(0.6)
    fscore = sscore*(0.2)
    total = round(shiny*sscore + pure*pscore + far*fscore)
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

async def exhardfunc(ctx, s, p, f, l):
    shiny = float(s)
    pure = float(p) - float(s)
    far = float(f)
    lost = float(l)
    ncount = shiny + pure + far + lost
    sscore = 10000000/ncount
    pscore = sscore*(0.5)
    fscore = 0
    total = round(shiny*sscore + pure*pscore + far*fscore)
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

async def chunifunc(ctx, s, p, f, l):    
    shiny = float(s)
    pure = float(p) - float(s)
    far = float(f)
    lost = float(l)
    ncount = shiny + pure + far + lost
    sscore = 101/ncount
    pscore = sscore*(100/101)
    fscore = sscore*(50/101)
    total = '%.4f' % (shiny*sscore + pure*pscore + far*fscore)
    grade = ""

    if total > 101:
        grade = ":place_of_worship: :place_of_worship: :place_of_worship: wait how did you get over 101%, please check your inputs!"
    elif total == 101:
        grade = ":regional_indicator_a: :regional_indicator_j: :regional_indicator_c: :tada:"
    elif total >= 100.75:
        grade = ":regional_indicator_s: :regional_indicator_s: :regional_indicator_s:"
    elif total >= 100:
        grade = ":regional_indicator_s: :regional_indicator_s:"
    elif total >= 97.5:
        grade = ":regional_indicator_s:"
    elif total >= 95:
        grade = ":a: :a: :a:"
    elif total >= 92.5:
        grade = ":a: :a:"
    elif total >= 90:
        grade = ":a:"
    elif total >= 80:
        grade = ":b: :b: :b:"
    elif total >= 70:
        grade = ":b: :b:"
    elif total >= 60:
        grade = ":b:"
    elif total >= 50:
        grade = ":regional_indicator_c:"
    else:
        grade = ":regional_indicator_d:"

    await ctx.channel.send("Chunithm Judge Score:\n" + grade + "  **" + str(total) + "%**")
