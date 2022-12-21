import sys
sys.path.append('E:\TeodorProgramming\Lab-08\package')

from package import add, minus, multiply, divide
print(f" 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")
x = int(input("Select operation: "))

if x == 1:
    a = float(input("Enter first num: "))
    b = float(input("Enter second num: "))
    print("The addition is ", add(a,b))
elif x == 2:
    a = float(input("Enter first num: "))
    b = float(input("Enter second num: "))   
    print("The substraction is ", minus(a,b))
elif x == 3:
    a = float(input("Enter first num: "))
    b = float(input("Enter second num: "))   
    print("The multiplication is ", multiply(a,b))
elif x == 4:
    a = float(input("Enter first num: "))
    b = float(input("Enter second num: "))
    from divideModule import divide     
    print("The division is ", divide(a,b))
else:
    print("Incorrect numbers")    

