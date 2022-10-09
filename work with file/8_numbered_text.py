FILE = "8_numbered_text.txt"
memory = []

with open(FILE, "r") as f:
    num = 1
    for line in f:
        memory.append(f"{num} " + line)
        num += 1

with open(FILE, "w") as f:
    for line in memory:
        f.write(line)
