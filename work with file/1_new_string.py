FILE = "1_new_string.txt"
string = "There should be a lot of strings!"

string = string.split()

with open(FILE, "w") as f:
    for i in string:
        f.write(i+"\n")
