__author__ = "Evren Aksuna"

while True:
    print("I am human: 1")
    print("I am created by someone: 2")
    print
    choose = input("Tell me what you are. 1 or 2? ")
    name = input("Tell me your name...")

    if choose == "1":
        print("Welcome to the Westworld, " + name + "!")
        print
        break
    elif choose == "2":
        print("Welcome to your home, " + name + "!")
        break
    else:
        print("You better go back to your world. Otherwise, I will have to destroy you.")
        break
