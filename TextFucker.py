import random
while True:
    x1 = input("Input text to fuck: ")
    y = x1.split(" ")
    for x in y:
        z = random.randint(0,100)
        print(x, end = "")
        print(" "*z, end = "")
    print()
