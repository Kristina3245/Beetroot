phone_number = input("Enter a phone number: ")
phone_length = 10
if phone_number.isdigit():
    if len(phone_number)!=10:
        print("Invalid phone number. Phone number must be 10 digits long.")
    else:
        print("Congrats! " + "Valid phone number.")
else: print("Invalid phone number. Phone number must contain only numerical characters.")

