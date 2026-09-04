#Write a program that asks the user for:

#Their age
#Whether they have a ticket
#Allow them to enter an event only if they are at least 14 and have a ticket.

age = int(input("What's your age? "))
ticket= (input("Do you have a ticket?"))
if age>=14 and ticket== "Yes":
    print("You can enter the event!")
else:
    print("Sorry! You can't go inside!")

