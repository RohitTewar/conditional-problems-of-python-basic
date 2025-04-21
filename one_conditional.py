# Program to check if a person is eligible to vote based on their age

# Input: Age of the person
age = int(input("Enter your age: "))

# Conditional check
if age < 18:
    print("You are child.")
elif age < 20:
    print("You are Teenager.")
elif age < 50:
    print("You are adult.")
else:
    print("You are senior citizen.") 
   
