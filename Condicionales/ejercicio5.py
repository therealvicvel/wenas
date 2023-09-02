num1=0
num2=0
resultado=0
num1=int(input("Ingrese el número 1: "))
num2=int(input("Ingrese el número 2: "))
if(num1<=0 and num2==0):
    print("No es posible divir por 0. ")
elif(num1>=0 and num2==0):
    print("No es posible divir por 0. ")
elif(num1<=0 and num2<=0):
    resultado=num1/num2
    print("El resultado es; " , resultado)
elif(num1>=0 and num2<=0):
    resultado=num1/num2
    print("El resultado es; " , resultado)
elif(num1<=0 and num2>=0):
    resultado=num1/num2
    print("El resultado es: " , resultado)
elif(num1>=0 and num2>=0):
    resultado=num1/num2
    print("El resultado es; " , resultado)