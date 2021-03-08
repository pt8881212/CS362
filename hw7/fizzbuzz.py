#Pratiksha Aga
# fizzbuzz
# homework 7

# function for fizzbuzz
def fbfunc(n):
    for i in range(1, 101): # numbers range from 1-100
        if i % 3 == 0 and i % 5 == 0: # if divisible by 3 and 5 then print
            print("FizzBuzz")
        elif i % 3 == 0: # if divisible by 3 then print
            print("Fizz")
        elif i % 5 == 0: # if divisible by 5 then print
            print("Buzz")
        else:
            return(i)
        i += 1;