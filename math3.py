import math
a = int(input("valor de a "))
b = int(input("valor de b "))
x = (a**b)/(b+4)
print(x)
y = (b**a)/(a+32)
print(y)
x = x / y
print(x)
raiz_quadrada = math.sqrt(x)
print(raiz_quadrada)
u = raiz_quadrada*math.pi
print(u)
