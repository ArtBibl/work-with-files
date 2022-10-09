while True:
    try:
        var = input("Enter power of a numbers ('q':Quit): ")
        if var == 'q':
            exit("Program complete!")
        var = int(var)
    except Exception:
        print("Only 'integer' number or 'q' for exit!")
        continue

    # print(f"{num} meters it`s a {num * 1000000000} nanometers.")
    print(f"{var} meters it`s a {int(var * 1e9)} nanometers.")
    print(f"{var} meters it`s a {var * 1000000} micrometers.")
    print(f"{var} meters it`s a {var * 100} centimeters.")
    print(f"{var} meters it`s a {var * 10} decimeters.")
    print(f"{var} meters it`s a {var} meters :) ")
    print(f"{var} meters it`s a {var * 0.001} kilometers.")





