fruit= str(input("Enter the fruit: "))
colour= str(input("Enter the colour: "))

if fruit == "banana":
    if colour == "green":
        print("Banana is unripe.")
    elif colour == "yellow":
        print("Banana is ripe.")
    elif colour == "black":
        print("Banana is overripe.")
        exit()
elif fruit == "orange":
    if colour == "green":
        print("Orange is unripe.")
    elif colour == "orange":
        print("Orange is ripe.")
    elif colour == "brown":
        print("Orange is overripe.")
        exit()
        
elif fruit == "apple":
    if colour == "green":
        print("Apple is unripe.")
    elif colour == "red":
        print("Apple is ripe.")
    elif colour == "brown":
        print("Apple is overripe.")
        exit()
elif fruit == "Mango":
    if colour == "green":
        print("mango is unripe.")
    elif colour == "yellow":
        print("mango is ripe.")
    elif colour == "black":
        print("mango is overripe.")
        exit()
else:
    print("Invalid fruit.")
    exit()