with open("windingwords.txt","r") as reader:
    lines = reader.readlines()
    linenum = 0
    wordlist = []
    for x in lines:
        splitted = x.split(',')
        wordlist.append(splitted[linenum%5].strip("\n"))
        linenum += 1
    highest = 0
    print(len(wordlist))
    for x in wordlist:
        if wordlist.count(x) >= highest:
            highest = wordlist.count(x)
            print(x,wordlist.count(x))
