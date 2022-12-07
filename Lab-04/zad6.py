n = int(input("Enter the count of elements: "))

list = []

for i in range(0,n):
    element = int(input("Enter an element: "))
    list.append(element)

print(list)
number = int(input("Enter 0 or 1: "))
for i in range(0,len(list)):
    if number == 0:
        if i % 2 == 0:
            list[i] += 5
    elif number == 1:
        if i % 2 == 1:
            list[i] += 10

print(list)