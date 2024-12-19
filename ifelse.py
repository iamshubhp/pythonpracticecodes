# if = Do some code IF some condition is true
# Else do something else

# lets create a credit card program where if the age is 18 or above the person is eligible if nahh than not eligible.

name = input("Enter you full name: ")
age = int(input("Enter your age to check if you are eligible: "))

if age >= 18:
    print(f"Hey {name}, Congratulations you are Eligible for the Credit Card")

elif age >= 24:
    print(
        f"Hey {name}, you are eligible for Credit Card along with premium Credit Limit")

else:
    print(f"Sorry {name} you are under 18 and not eligible for the Credit Card")

# Easiest example to understand how If ElIf Else Statements work :)

# We can add as many ElseIf statement as we want
