import math

a = int(input("Enter number: "))
try:
    if a < 0:
        raise ValueError
    print(math.sqrt(a))
except ValueError:    
    print(a,"is invalid number")  
finally:
    print("Good bye")   

      