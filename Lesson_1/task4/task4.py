
print("Калькулятор квадратних рівннянь")

a = int(input("Введіть число ax^2: "))
b = int(input("Введіть число bx: "))
c = int(input("Введіть число с "))

D = (b**2)-(4*a*c)
print(D)

x = (-b / 2*a)
x1 = (((-b)-(D**0.5))/(2*a))
x2 = (((-b)+(D**0.5))/(2*a))
#print(x)
#print(x1)
#print(x2)

if D<0:
    print("Немає коренів")
elif D==0:
    print(x)
elif D>0:
    print(x1,x2)
