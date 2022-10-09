FILE = "5_ten_numbers.txt"

with open(FILE, "r") as f:
    var = f.readline().split()
    print(var)
