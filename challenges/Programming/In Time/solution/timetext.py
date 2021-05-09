with open("time.txt","r") as reader:
    lines = reader.readlines()
    split = lines[0].split(',')
    for x in split:
        if x != "timetimetimetimetime":
            print(x)
