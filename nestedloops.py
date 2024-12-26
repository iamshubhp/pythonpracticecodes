# nested loop = A loop within another loop(outer, inner)
#               outer loop:
#                   inner loop:


# for x in range(3):
#     for y in range(1, 10):

#         # end = "" will get the output in one line. we can add symbols or space between the ""
#         print(y, end="")

#     print()  # this print statement is for the outer loop which will get the output one below another

# -------------------------------------------------------------------------------------------------------

# Practice program to print the symbols entered as a rectangle


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
