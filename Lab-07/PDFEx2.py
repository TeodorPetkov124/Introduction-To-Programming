try:
    f = open("demofile.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("No such file")
    f.close()