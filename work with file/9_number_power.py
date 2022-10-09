FILE = "9_number_power.txt"
memory = []

while True:
    try:
        num = input("Enter the number ('q'-stop and write): ")
        if num == 'q':
            break
        num = float(num)
        memory.append(f"{num} -> {num ** 2} -> {num ** 3}")
    except Exception:
        print("Exception: Only number or 'q' for stop!")
        continue

with open(FILE, "a") as f:
    for i in memory:
        f.write(f"{i}\n")
