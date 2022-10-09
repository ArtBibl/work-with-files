FILE = "6_lower_string.txt"

with open(FILE, "r") as f:
    lover = f.readline()

with open(FILE, "a") as f:
    f.write(f"\n{lover.upper()}\n")
    f.write(f"{lover.lower()}\n")

