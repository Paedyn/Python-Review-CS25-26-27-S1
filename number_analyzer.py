ask=(int(input("How many numbers would you like?")))
for i in range(ask): #why add i
    number= (int(input("Enter a number:")))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
        if number % 2==0:
            print("Even")
        else:
            print("Odd")