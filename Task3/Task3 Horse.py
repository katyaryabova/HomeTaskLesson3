x1 = int(input("Enter number: "))
x2 = int(input("Enter number: "))
y1 = int(input("Enter number: "))
y2 = int(input("Enter number: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("OK")
else:
    print("FALSE")
