#program to create a strong security password
# specifying the list of special characters that should be in the password
Specialsymbols =['$','@','#','!']
while True:
    #first step giving the required password as an input
    password = input("enter a password :")
   #To check whether the entered string is 6 characters or not
    if len(password) < 6:
        print("Weak Password : Password Should be of atleast 6 characters long ")
        continue
    #To check whether the entered string exceeds 16 characters
    elif len(password) > 16:
        print("Length Exceeded: Password can have utmost 16 characters ")
        continue
    #To check if that the entered string should have at least one number
    elif not any(char.isdigit() for char in password):
        print('the password should have at least one numeral')
        continue
    #To check if the entered string should have at least one uppercase letter
    elif not any(char.isupper() for char in password):
        print('the password should have at least one uppercase letter')
        continue
    #To check the entered string should have at least one lower case letter
    elif not any(char.islower() for char in password):
        print('the password should have at least one lowercase letter')
    #To check that there should be atleast one special symbol in password
        continue
    elif not any(char in Specialsymbols for char in password):
        print('the password should have at least one of the symbols $@#!')
        continue
    else:
        print("The entered password meets all security requirements")
        print(password)
        break