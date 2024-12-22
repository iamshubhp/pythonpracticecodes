# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter the username: ")

if len(username) > 12:
    print("More than 12 letters is not allowed!")

elif not username.find(" ") == -1:  # if the result is not -1 we found a space
    print("your username contains space and it is not allowed")

# if the result is not alphabet or contains any digit it will find it.
elif not username.isalpha():
    print("Digits are not allowed!")

else:
    print("The Username is Valid!")
