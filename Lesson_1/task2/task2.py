print("Калькулятор")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
s = input("Введіть дію +,-,*,/,** - Степінь,// - Корінь: ")

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

