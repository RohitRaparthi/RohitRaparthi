a = float(input())
b = float(input())
operation = input()
if operation == "add":
    print(a + b)
elif operation == "sub":
    print(a - b)
elif operation == "mul":
    print(a * b)
elif operation == "div":
    if b != 0:
        print(a / b)
    else "Cannot divide by zero"