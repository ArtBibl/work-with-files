CHAR = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

while True:
    try:
        four_words = input("Enter 4 words ('q':Quit):")
        if four_words == 'q':
            exit("Program complete!")
        four_words = four_words.split()

        if len(four_words) != 4:
            raise Exception

        for i in four_words:
            if i.lower()[0] not in CHAR:
                raise Exception
        four_words.sort()
        for i in four_words:
            print(i)

    except Exception:
        print("Try again! Just 4 words, it's easy :)")
        continue
