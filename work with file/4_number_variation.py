FILE = "4_number_variation.txt"

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        break
    except ValueError:
        print("Exception: Only numbers! Try again.")
        continue

with open(FILE, "w") as f:
    """I hope we don't have another solution to get this task"""
    """Looks like it`s not so smart solution"""
    f.write(f"{num1}, {num2}, {num3}\n")
    f.write(f"{num1}, {num3}, {num2}\n")
    f.write(f"{num2}, {num1}, {num3}\n")
    f.write(f"{num2}, {num3}, {num1}\n")
    f.write(f"{num3}, {num1}, {num2}\n")
    f.write(f"{num3}, {num2}, {num1}\n")

