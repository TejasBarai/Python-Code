Calculator = True
while(Calculator):
    choice = int(input("\n 1)Add \n 2)Sub \n 3)Mul\n 4)Div \n 5)Exit \n Select any one Option"))
    if(choice ==1):
        num1 = int(input("Enter the first Number: "))

        num2 = int(input("Enter the Second Number: "))

        print (num1 + num2)




    elif(choice== 2):
        nunl= int (input("Enter the first Number: "))
        

        num2 =int(input("Enter the Second Number: "))

        print (num1 - num2)




    elif(choice == 3):

        num1 = int(input("Enter the first Number :"))
        num2= int(input("Enter the Second Number: "))
        print (num1 * num2)

    elif(choice == 4):

        num1 = int(input("Enter the first Number :"))
        num2= int(input("Enter the Second Number: "))
        print (num1 / num2)

    elif(choice==5):
        print ("Invalid Choice")
        Calculator = False
    
    else:
        print("Invalid choice....\nplease currect choice")

    print("---------------------------------------------------------")    








    

