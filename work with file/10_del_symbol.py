FILE = "10_del_symbol.txt"
memory = []

with open(FILE, "r") as f:
    for line in f:
        if line[0] != "#":
            memory.append(line)

with open(FILE, "w") as f:
    for line in memory:
        f.write(line)
