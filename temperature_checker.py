#"Very hot" if the temperature is 30 or higher.
#"Warm" if the temperature is 20 or higher.
#"Cool" if the temperature is 10 or higher.
#"Cold" otherwise.

temp = int(input("Enter the temperature: "))

if temp >= 30:
    print("Very hot!")
elif temp >= 20:
    print("Warm!")
elif temp >= 60:
    print("Cool :)")
else:
    print("Cold :(")