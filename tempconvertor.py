# Temperature convertor program basic

unit = input("is this Temperature in Celcius or Fahrenheit (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == "f":
    c = (temp - 32) * 5/9
    unit = "°C"
    print(f"The temperature in Fahrenheit will be {c} {unit}")

elif unit == "c":
    f = (temp * 9/5) + 32
    unit = "°F"
    print(f"The temperature in Celcius will be {f} {unit}")

else:
    print(f"{temp} is invalid!")
