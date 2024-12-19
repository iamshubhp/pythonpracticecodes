# Weight Convertor from Grams to KG and KG to grams

weight = float(input("Enter the Weight: "))
unit = input("kilograms or grams (k / g): ")

if unit == ("k"):
    result = weight * 1000
    unit = "grams"
    print(f"your weight is {result} {unit}")

elif unit == "g":
    result = weight / 1000
    unit = "kilograms"
    print(f"your weight is {result} {unit}")

else:
    print(f"{unit} is not valid!")
