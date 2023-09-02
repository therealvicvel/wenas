num1=0
num2=0
num1=int(input("Ingrese el número 1: "))
num2=int(input("Ingrese el número 2: "))
if(num1<=0 and num2<=0):
    print("No hay resultados para mostrar. ")
elif(num1>=0 and num2>=0):
    print("No hay resultados para mostrar. ") 
elif(num1<=0 and num2>=0):
    print("El número 1 es: " , num1)
    print("El número 2 es: " , num2)
elif(num1>=0 and num2<=0):
    print("El número 1 es: " , num1)
    print("El número 2 es: " , num2)