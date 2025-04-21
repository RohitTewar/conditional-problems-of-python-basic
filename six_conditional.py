distance = int(input("Enter the distance in meters: ")) 

if distance < 100:
    transport ="You can walk." 
elif distance < 1000:
    transport ="You can ride a bicycle."    
elif distance < 10000:
    transport ="You can take a bus."     
else:
    transport ="You can take a train " 

print("recommended transport for you:",transport)