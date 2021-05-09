folder_path = "C:\\Users\\wben1\\Desktop\\zip"

fake = None

for i in range(50000):
    with open(f"{folder_path}\\{i}.txt", "r") as text_file:
        flag = text_file.read()
        if not fake:
            fake = flag
            continue
    
    if fake != flag:
        print(flag)
        break