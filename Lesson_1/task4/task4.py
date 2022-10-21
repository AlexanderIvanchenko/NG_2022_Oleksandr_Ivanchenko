
print("Calculator of quadratic equations")

a = int(input("Enter ax^2: "))
b = int(input("Enter bx: "))
c = int(input("Enter с "))

D = (b**2)-(4*a*c)
print(D)

x = (-b / 2*a)
x1 = (((-b)-(D**0.5))/(2*a))
x2 = (((-b)+(D**0.5))/(2*a))

if D<0:
    print("no roots")
elif D==0:
    print(x)
elif D>0:
    print(x1,x2)
