import getpass
user1=input("Please Enter Player 1 Name:- ")
user2=input("Please Enter Player 2 Name:- ")
a=0
b=0
for i in range(0,5):
    c1= getpass.getpass(user1+" Please Choose(stone/paper/scissor):- ")
    c2=getpass.getpass(user2+" Please Choose(stone/paper/scissor):- ")
    if c1=="stone" and c2=="stone":
        print("Game Tie")
    elif c1=="stone" and c2=="paper":
        b=b+1
        print(user2,"Won")
    elif c1=="stone" and c2=="scissor":
        a=a+1
        print(user1,"Won")
    elif c1=="paper" and c2=="paper":
        print("Game Tie")
    elif c1=="paper" and c2=="scissor":
        b=b+1
        print(user2,"Won")
    elif c1=="paper" and c2=="stone":
        a=a+1
        print(user1,"Won")
    elif c1=="scissor" and c2=="scissor":
        print("Game Tie")
    elif c1=="scissor" and c2=="stone":
        b=b+1
        print(user2,"Won")
    elif c1=="scissor" and c2=="paper":
        a=a+1
        print(user1,"Won")
    else:
        print("Please Give Right Input")
if a<b:
    print(user2,"Won the Game with",b,"Points")
elif a>b:
    print(user1,"Won the Game with",a,"Points")
else:
    print("Finally Game Tie")
