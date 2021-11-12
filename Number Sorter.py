print("Hi, please add some numbers to the list!")
print("When you're finished type 'sort' to sort it!")

number_list = []

def Check_Int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def List_Sort(list1):
    list2 = []
    for i in list1:
        list2.append(i)
    print(list2)
        
while True:
    number = str(input(" >>> "))
    if number == "sort":
        List_Sort(number_list)
        break
    test = Check_Int(number)
    if test == False:
        print("That's not a valid input.")
        continue
    else:
        number_list.append(int(number))
        print("Added(" + str(number) + ")")
        print(number_list)
    
    
