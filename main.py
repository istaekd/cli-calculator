a = int(input("First number: "))
b = int(input("Second number: "))
c = input("Operator: ")

if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "x":
    result = a * b
elif c == "/":
    result = a / b
else:
    result = "Wrong inputs"

print(f"Result: {result}")