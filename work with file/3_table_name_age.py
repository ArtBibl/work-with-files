FILE = "3_table_name_age.txt"

name = input("Enter a name: ")
age = input("Enter age: ")
profession = input("Enter profession: ")

with open(FILE, "w") as f:
    f.write(f'Name\tAge\tProfession\n{name}\t{age}\t{profession}')
