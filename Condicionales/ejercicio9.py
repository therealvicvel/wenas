num1=0
num2=0
num1=int(input("Ingrese el número 1: "))
num2=int(input("Ingrese el número 2: "))
if(num1<num2):
    print("Primero iría: " , num1)
    print("Y después: " , num2)
elif(num1>num2):
    print("Primero iría: " , num2)
    print("Y después: " , num1)
elif(num1==num2):
    print("Ambos números son iguales. ")