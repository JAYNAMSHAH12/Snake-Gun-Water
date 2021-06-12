#Snake Water Gun

# snake and water : snake
# snake and gun   : gun
# water and gun   : water

import random
i=0
computer_point=0
your_point=0
while(i<10):
    i = i + 1
    print(i,"of 10 rounds ")


    lst=["Snake","Water","Gun"]
    choice=random.choice(lst)
    # print("Computer's Choice is :",choice)
    print("Enter the Number For choice:\n","1 for Snake \n 2 for Water\n 3 for Gun \n")
    choose=int(input("Your Choice is:"))
    print("Computer's Choice is :",choice)




    if choose==1 and choice=="Water":
        your_point=your_point+1
        print("You Wins This Round and rewarded with 1 point ")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose == 1 and choice == "Gun":
        computer_point=computer_point+1
        print("Computer Wins This Round and rewarded wih 1 point")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose==3 and choice=="Water":
        computer_point = computer_point + 1
        print("Computer Wins This Round and rewarded wih 1 point")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose==3 and choice=="Snake":
        your_point = your_point + 1
        print("You Wins This Round and rewarded with 1 point ")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose==2 and choice=="Snake":
        computer_point = computer_point + 1
        print("Computer Wins This Round and rewarded wih 1 point")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose==2 and choice=="Gun":
        your_point = your_point + 1
        print("You Wins This Round and rewarded with 1 point ")
        print(f"Computer point is {computer_point} and Your Point is {your_point}")
        print("----------------------------------------------------------------------------")
    elif choose == choice:
        print("Tie 0 points to Each")
    else:
        print("Please Enter Valid Choice")
        print("----------------------------------------------------------------------------")


if computer_point==your_point:
    print("Game Tied")
    print("----------------------------------------------------------------------------")

elif computer_point>your_point:
    print("Computer Wins The Game Better Luck Next Time!!!")
    print("----------------------------------------------------------------------------")

else:
    print("Congratulations!! You Won The Game")
    print("----------------------------------------------------------------------------")

print("Game Over")




