import random
score = 0
while True:
    i = random.randint(0,2) #Entekhab CPU
    choises = ["Sang","Kagaz","Geychi"]
    print("1- Sang \n2-Kagaz \n3-Geychi")
    inp = input("Enter a Number:")
    if(inp == "score"):
        print("Your Score: {0}\n".format(str(score)))
        continue
    else:
        inp = int(inp)
        inp = inp -1
        print("================")
        print("CPU Choise:{0}".format(choises[i]))
        if inp == 0 and i == 2 or inp == 1 and i == 0 or inp == 2 and i == 1:
            #WIN
            print("Win")
            score = score + 10
        elif inp == 0 and i == 1 or inp == 1 and i == 2 or inp == 2 and i == 0:
            #LOSE
            print("Lose")
            score = score - 5
        elif inp == i:
            #SAME
            print("Same")
        else:
            print("\nError\n")
