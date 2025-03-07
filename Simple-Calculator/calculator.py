def add(x,y):
    return x+y 
def subtract(x,y):
    return x-y 
def multiply(x,y):
    return x*y 
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error: Cannot divide by zero!"

print("welcome to the simple calculator")
print("Operations: 1] Add , 2] Subtract , 3] Multiply , 4] Division") 

a = float(input("enterr your first number: "))
c = int((input("enterr your operation [1-4]: ")))
b = float(input("enterr your second number: ")) 

if c ==1:
    r = add(a,b)
    print(f"{a} + {b} = {r}")
elif c ==2:
    r = subtract(a,b)
    print(f"{a} - {b} = {r}")
elif c ==3:
    r = multiply(a,b)
    print(f"{a} * {b} = {r}")
elif c ==4:
    r = divide(a,b)
    print(f"{a} / {b} = {r}")
else:
    print("Invalid operation choice!")