#7.	Leer el nombre de un empleado, el salario básico por hora y el número de horas trabajadas durante una
# semana. Calcular el salario neto, teniendo en cuenta que si el número de horas trabajadas durante la semana es mayor a 48, esas horas de mas
# se consideran horas extrasy tienen un 25% de recargo.
nombreEmpleado=""
salarioBasico=0
horasTrabajadas=0
salarioNeto=0
recargo=0
horasExtra=0
nombreEmpleado=input("Señor empleado, ingrese su nombre: ")
salarioBasico=int(input("¿Cuánto es su salario básico? "))
horasTrabajadas=int(input("¿Cuántas horas a la semana trabaja? "))
if(horasTrabajadas<=48):
    salarioNeto=salarioBasico*horasTrabajadas
    print("Su salario es: " , salarioNeto)
elif(horasTrabajadas>=48):
    horasExtra=salarioBasico-horasTrabajadas
    recargo=(salarioBasico*horasExtra)*0.25
    salarioNeto=(salarioBasico*horasTrabajadas)+recargo
    print("Su salario neto es: " , salarioNeto)