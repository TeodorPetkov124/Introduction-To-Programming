x = str(input("Enter a figure: "))

if x == "rectangle":
   a = float(input("Enter a: "))
   b = float(input("Enter b: "))
   from rectangleArea import rectangle
   print("The are of the rectangle is", rectangle(a, b))
elif x == "triangle":
    a = float(input("Enter a: ")) 
    b = float(input("Enter b: ")) 
    from triangleArea import triangle
    print("The are of the triangle is", triangle(a,b))
elif x == "square":
    a = float(input("Enter a: "))
    from suqareArea import square
    print("The are of the square is", square(a))
elif x == "rhombus":
    a = float(input("Enter a: ")) 
    from rhombusArea import rhombus
    print("The are of the rhombus is", rhombus(a))    
elif x == "trapezoid":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    from trapezoidArea import trapezoid
    print("The are of the trapezoid is", trapezoid(a, b, h))



   

   