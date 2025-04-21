weather = str(input("Enter the weather: "))
#temperature = int(input("Enter the temperature: ")) 
if weather == "sunny":
    print("You can go for a walk.")
elif weather == "rainy":
    print("You can go for a walk with an umbrella.")
elif weather == "cloudy":
    print("You can go for a walk with a jacket.")
elif weather == "snowy":
    print("You can go for a walk with a snow jacket.")  
elif weather == "stormy":
    print("You can go for a walk with a rain jacket.")
else:
    print("Invalid weather condition.")
    exit()