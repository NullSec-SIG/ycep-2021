#RiddleSolver
with open("riddletext.txt","r") as file:
    line = file.readline()
    nline = line[24::25]
    print(nline)
    fline = ""
    for x in range(len(nline)):
        if nline[x].isdigit() == True:
            print(nline[x])
            fline += str(int(nline[x])-3)
        else:
            fline += nline[x]
    print(fline[::-1])

#Capitalisation can be done manually
