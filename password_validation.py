
def password_validation(password):
    lenght = len(password)
    upper = False
    digit = False
    if lenght > 7:
        for char in password:
            if char.isupper():
                upper = True
            if char.isdigit():
                digit = True

    if upper and digit:
        password_is_valid = True
    else:
        password_is_valid = False

    return password_is_valid

user_password = False

while user_password is False:

    password_input = input("Enter a password: ")

    user_password = password_validation(password_input)

    if user_password:
        print("Password accepted")
    else:
        print("Password not accepted - enter a password with has minimum eight characters, "
              "one upper character and one digital character.")

