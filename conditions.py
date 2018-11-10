print("Enter 1 for door")
print("Enter 2 for window")


"""Note it is elif instead of else if"""
option = int(input(">"))
if option == 1:
    print("You have chosen door")
elif option == 2:
    print("You have chosen window")
else:
    print("Not valid choice")