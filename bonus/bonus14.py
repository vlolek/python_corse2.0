from converters import convert
from parsers14 import parse
feet_inches = input("Enter feet and inches:")

feet, inches = parse(feet_inches)

result = convert(feet, inches)


print(f"{feet} feet and {inches}  is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.") 