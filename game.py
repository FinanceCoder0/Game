Games=["1 = Rock,Paper,Scissor","2 = Number Guseeing Game"]
print(Games)
print("Chose 1 or 2")
Game=input("Which Game do you want to play?" )
game=int(Game)
if Game=="Rock,Paper,Scissor" or game==1:
    import random
    list=["rock", "paper", "scissor"]
    x = random.choice(list)
    y =input("rock,paper,scissor:")
    if x=="rock" and y=="paper":
        print("You win ")
        print("You win ")
        print("Computer choose:",x)
    elif y=="rock" and x=="paper":
        print("Computer win ")
        print("Computer choose:",x)
    elif x=="rock" and y=="scissor":
        print("Computer win")
        print("Computer choose:",x)
    elif y=="rock" and x=="scissor":
        print("You win")
        print("Computer choose:",x)
    elif x=="paper" and y=="scissor":
        print("You win")
        print("Computer choose:",x)
    elif y=="paper" and x=="scissor":
        print("Computer win")
        print("Computer choose:",x)
    else:
        print("Both choices are same")
        print("Computer choose:",x)
else:
    import random
    s=5
    x=int(input("Minimum Range:"))
    y=int(input("Maximum Range:"))
    z= random.randint(x,y)
    print("You have",s,"lifes")
    a=int(input("Enter guess"))
    print(z)
    while a!=z:
        if a!=z and s!=0:
            print("Try Again")
            s-=1
            print("Now,you have",s,"Life")
            a=int(input("Enter guess"))
        elif a!=z and s==0:
            print("You are fail")
            print("The correct number is:",z)
            break
    else:
            print("You have done")