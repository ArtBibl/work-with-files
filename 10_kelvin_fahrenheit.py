""" int + K, F, C"""

while True:
    try:
        request = input("Enter temperature and index:'K' or 'F' or 'C' ('q':Quit):")
        if request == 'q':
            exit("Program complete!")
        request = request.split()
        if len(request) > 2:
            raise Exception
        temp = float(request[0])
        ind = request[1]

        if ind == 'C':
            print(f"{temp}{ind} = {round(temp * 1.8 + 32, 2)}F")
            print(f"{temp}{ind} = {round(temp + 273.15, 2)}K")
        elif ind == 'K':
            print(f"{temp}{ind} = {round(temp - 273.15, 2)}C")
            print(f"{temp}{ind} = {round(1.8 * (temp - 273.15) + 32, 2)}F")
        elif ind == 'F':
            print(f"{temp}{ind} = {round((temp - 32) / 1.8, 2)}C")
            print(f"{temp}{ind} = {round((temp - 32) * 5/9 + 273.15, 2)}K")
        else:
            raise Exception

    except Exception:
        print("Exception: Try again! Temperature + space + 'K' or 'F' or 'C'.")
        continue
