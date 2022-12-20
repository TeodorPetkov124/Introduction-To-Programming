from rectangleArea import rectangle
from triangleArea import triangle
from suqareArea import square
from rhombusArea import rhombus
from trapezoidArea import trapezoid

x = str(input("Enter a figure: "))

if x == "rectangle":
   a = float(input("Enter a: "))
   b = float(input("Enter b: "))
   print("The are of the rectangle is", rectangle(a, b))
elif x == "triangle":
    a = float(input("Enter a: ")) 
    b = float(input("Enter b: ")) 
    print("The are of the triangle is", triangle(a,b))
elif x == "square":
    a = float(input("Enter a: "))
    print("The are of the square is", square(a))
elif x == "rhombus":
    a = float(input("Enter a: ")) 
    print("The are of the rhombus is", rhombus(a))    
elif x == "trapezoid":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    print("The are of the trapezoid is", trapezoid(a, b, h))



   

   