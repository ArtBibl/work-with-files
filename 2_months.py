# MONTHS = ("January", "February", "March", "April", "May", "June", "July",
#           "August", "September", "October", "November", "December")

PERIOD = ("Winter", "Spring", "Summer", "Autumn")

while True:
    try:
        num = input("Enter number of month ('q':Quit): ")
        num = int(num) if num != 'q' else exit("Program complete!")
        # print(f"{MONTHS[num - 1]}")
        if num == 12 or num == 1 or num == 2:
            print(PERIOD[0])
        elif 3 <= num <= 5:
            print(PERIOD[1])
        elif 6 <= num <= 8:
            print(PERIOD[2])
        elif 9 <= num <= 11:
            print(PERIOD[3])
        else:
            raise Exception
    except Exception:
        print("Use only numbers from 1 to 12!")
