#Int + length check

StudentNumber = ""
number = False
while len(str(StudentNumber)) != 6 or  number == False:
    StudentNumber = str(input("Please enter a 6-digit student number:"))
    if len(str(StudentNumber)) == 6:
        try:
            int(StudentNumber)
        except ValueError:
            print("This isn't a number")
        else:
            StudentNumber = int(StudentNumber)
            number = True
            break
    print ("That wasn't 6 digits!")
print(f"You entered the student number: {StudentNumber}")

#Capital letter password check

print("Enter a Password containing at least one capital letter.")
password = input(" >>> ")
passwordValid = False
while not passwordValid:
    for index in range(len(password)):
        if ord(password[index]) in range (65, 91):
            passwordValid = True
    if not passwordValid:
        password = input("Invalid - please enter a new password: ")
print("Password Accepted")
