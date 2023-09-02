num1=0
num2=0
resultado=0
num1=int(input("Digite el número 1: "))
num2=int(input("Digite el número 2: "))
if(num2==0):
    print("No podemos realizar este proceso porque la división por 0 no existe")
else:
    resultado=(num1/num2)
    print("El resultado de la división es: " , resultado)