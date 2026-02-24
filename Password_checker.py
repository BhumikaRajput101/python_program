def is_strong_pasword(password):
    if len(password)<8:
        print("Must contain upto 8 characters")
    elif not any(char.isdigit() for char in  password):
        print("Must have 1 digit")
    elif not any(char.islower() for char in password):
        print("Must have 1 lower case alphabet")
    elif not any(char.isupper() for char in password):
        print("must have 1 upper case alphabet")
    elif not any(char in "!@#$%^&*_+" for char in password):
        print("Must have a special character")
    else :
       print("You have a strong password") 
password=input("Enter a password:")
is_strong_pasword(password)    