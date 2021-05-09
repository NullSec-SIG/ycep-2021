with open("thegreatnumberwall.csv","r") as file:
    lines = file.readlines()
    pline = lines[0].strip("\n").split(",")
    print(pline)
    for i in range(0, len(pline)):
        pline[i] = int(pline[i])
    
    
    #each line
    for x in range(1,len(lines)):
        cline = lines[x].strip("\n").split(",")
        for i in range(0, len(cline)):
            cline[i] = int(cline[i])
        #each number
        for y in range(len(cline)):
            #check which is higher
            #check if on the edge
            if y == 0:
                cline[y] = max(pline[y]+cline[y],pline[y+1]+cline[y])
            elif y == len(cline)-1:
                cline[y] = max(pline[y-1]+cline[y],pline[y]+cline[y])
            else:
                cline[y] = max(pline[y-1]+cline[y],pline[y]+cline[y],pline[y+1]+cline[y])
        #shifts current line into previous line
        pline = cline
    print(max(cline))
    
