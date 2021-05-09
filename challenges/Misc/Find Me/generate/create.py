import os

os.mkdir("zip")

index = 27386
fake = "HNF{is_This_the_0n3?}"
real = "HNF{is_Th1s_the_On3?}"

for i in range(50000):
    with open(f"zip/{i}.txt", "w") as text_file:
        if i == index:
            text_file.write(real)
        else:
            text_file.write(fake)