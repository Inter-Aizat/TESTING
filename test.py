name = []

with open(r"E:\WORK\Text\INPUT\C10OCT22.txt", 'r') as file:
    # print(file.readlines())
    for count, line in enumerate(file):
        if "CH00000" in line[0:21]:
            # name = line[48:88]
            name.append(line[40:88])

print(name)
for names in name:
    names.rsplit()
    print(names)