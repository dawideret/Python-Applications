Loop = True  #I'm setting the Loop variable to always be true to use it later.

def CheckFloat(x):  #I define a function called CheckFloat that takes an argument x into it.
    try:
        float(x)  #I check if the value x can be changed into a float or not and return True or False.
        return True
    except ValueError:
        return False

while Loop == True:  #I start a loop which will repeat itself as long as Loop variable is True.
    print("=========================================")  #I display a text message to a user to convey what I want from them.
    print("What do you want to do? (Enter a Number!)")
    print("1. Add")  #I give the user a number of options to choose from.
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Mod")
    print("6. Quit")
    choice = input("Input >>> ")  #I ask the user for an input.
    if choice == "6":  #If input is 6 I break the loop and quit the program.
        Loop = False
        break
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":  #I check if the input user gave us is on the list of choices.
        print("=========================")  #If the user input is not on the list of choices I notify him about it.
        print("=========================")
        print("Wrong Input! Try Again...")
        print("=========================")
    else:
        choice = float(choice)  #If the users input is on the list I change its format from string to float.
        
        print("Input first number")
        first = input("Input >>> ")  #I ask the user to input the first number.
        isValid = CheckFloat(first)  #I call out previously defined function called "CheckFloat" giving it variable "first" as the "x" it requires.

        if isValid == True:  #If my function returned true I continue and do the same for the second number.
            print("Input second number")
            second = input("Input >>> ")
            if second == "0" and choice == 4:  #If the user tried to divide by 0 I stop it and go back.
                print("=========================")
                print("=========================")
                print("Can't divide by 0! Try Again...")
                print("=========================")
                continue
                
            isValid = CheckFloat(second)

            if isValid == True:  #If the second Number can also be converted into a float I continue further.

                first = float(first)  #I change the first and second number our user gave us from a string to float.
                second = float(second)
                
                if choice == 1:  #I check what the choice previously was and use the correct calculation.
                    calc = first + second  #I put the result of the calculation into a variable called calc.
                    proofing = True  #This bit is a bit redundand and not fully neccessary. I check to make sure the calculation actually happened.
                if choice == 2:
                    calc = first - second
                    proofing = True
                if choice == 3:
                    calc = first * second
                    proofing = True
                if choice == 4:
                    calc = first / second
                    proofing = True
                if choice == 5:
                    calc = first % second
                    proofing = True
                if proofing == True:  #If any of the calculations happened I print out the result in a message.
                    print("The number calculated is >>> " + str(calc) + " <<<")
                    print("=========================================")
            else:  #If the user input couldn't be changed into a float I notify the user.
                print("=========================")
                print("=========================")
                print("Wrong Input! Try Again...")
                print("=========================")
        else:  #If the user input couldn't be changed into a float I notify the user.
            print("=========================")
            print("=========================")
            print("Wrong Input! Try Again...")
            print("=========================")
quit()
