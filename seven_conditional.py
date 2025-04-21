Coffee_order_size = str(input("What size coffee would you like? (small, medium, large): "))

extra_shot = str(input("Would you like an extra shot of espresso? (yes/no): ")) 

if extra_shot == "yes":
    if Coffee_order_size == "small":
        price = 3.50 + 0.50
    elif Coffee_order_size == "medium":
        price = 4.00 + 0.50
    elif Coffee_order_size == "large":
        price = 4.50 + 0.50
    else:
        print("Invalid size.")
        exit()
elif extra_shot == "no":
    if Coffee_order_size == "small":
        price = 3.50
    elif Coffee_order_size == "medium":
        price = 4.00
    elif Coffee_order_size == "large":
        price = 4.50
    else:
        print("Invalid size.")
        exit()
else:
    print("Invalid input for extra shot.")
    exit()
print(f"Your total price is: ${price:.2f}")