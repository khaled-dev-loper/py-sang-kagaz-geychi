import random
score = 0
version = "1.0"
while True:
    print("--{ use -h for Help }--")
    i = random.randint(0,2) #Entekhab CPU
    choises = ["Sang","Kagaz","Geychi"]
    print(*list(map(lambda a:str(a[0] + 1)+"- "+a[1]+"\n",enumerate(choises))),sep="")
    inp = input("Enter a Number:")
    if("-h" in inp):
        print("""
commands:
  [-h]  help
  [-s]  show score
  [-v]  version
Created by Khaled Developer

""")
        continue
    elif ("-s" in inp):
        print("Your Score: {0}\n".format(str(score)))
        continue
    elif ("-v" in inp):
        print("Version: {0}\n".format(version))
        continue
    else:
        try:
            inp = int(inp) -1
        except ValueError:
            print("*[ERROR]: only number you used \"{0}\".".format(type(inp).__name__))
            continue
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
