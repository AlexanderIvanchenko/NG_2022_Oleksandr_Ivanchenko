print("Calculator")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
s = input("Enter an action +,-,*,/,** - exponentiati,// - root: ")

if s =="+":
    print(a + b)
elif s =="-":
    print(a - b)
elif s =='*':
    print(a * b)
elif s =="/":
    print(a / b)
elif s == "**":
    print(a ** b)
elif s =="//":
    print(a**(1/b))

