# Function to addition  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtraction 
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiplication 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to division
def divide(num1, num2): 
    return num1 / num2 

# Printing the first line for the first number input
nu1 = int(input("Enter first number: "))

# display message for user to pick an operand
print("\nEnter the number for which operation you would like to chose-\n" 
        "1. +\n" 
        "2. -\n" 
        "3. x\n" 
        "4. /\n") 
  
  
# Take input from the user for the operand
select = int(input("")) 
 
# Take input from the user for the second number
nu2 = int(input("\nEnter second number: ")) 
  
# if select is equal to operand one then add number 1 and number 2
if select == 1: 
    print("\nAnswer:")
    print(nu1, "+", nu2, "=", 
                    add(nu1, nu2)) 
  
# Else if select is equal to 2 then subtract number 1 and 2 
elif select == 2: 
    print("\nAnswer:")
    print(nu1, "-", number_2, "=", 
                    subtract(nu1, nu2)) 
  
# Else if select is 3 then multiply number 1 and number 2
elif select == 3: 
    print("\nAnswer:")
    print(nu1, "*", nu2, "=", 
                    multiply(nu1, nu2)) 
  
# Else if select is equal to 4 then divide number 1 and number 2
elif select == 4: 
    print("\nAnswer:")
    print(nu1, "/", nu2, "=", 
                    divide(nu1, nu2)) 
else: 
    print("Invalid input") 