number = int(input("Enter a percentage from 0% to 100%: "))

while number < 0 or number > 100:
    print("Invalid number.")
    number = int(input("Enter a number percentage from 0% to 100%: "))

print(f"You entered {number}%.")