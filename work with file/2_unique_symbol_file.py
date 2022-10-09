FILE = "2_unique_symbol_file.txt"

string = input("Enter your string: ")

string = set(string)

with open(FILE, "w") as f:
    for i in string:
        f.write(i+"\n")
