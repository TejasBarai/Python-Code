Calculator=True
while(Calculator):
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the Second Number: "))
    choice = int(input("\n 1)Add \n 2)Sub \n 3)Mul\n 4)Div \n 5)Reminder \n 6)Exit \n Select any one Option :"))
    if(choice ==1):
        print (num1 + num2)
    
    elif(choice ==2):
        print (num1 - num2)

    elif(choice ==3):
        print (num1 * num2)   

    elif(choice ==4):
        print (num1 / num2)
    
    elif(choice==5):
        print(num1%num2)

    elif(choice ==6):
        print ("Thank you for using calculator")
        Calculator = False

    else:
        print("Invalid choice....\nplease currect choi")

    print("-----------------*********------------------\n")    