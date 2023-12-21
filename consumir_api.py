import requests

# Hacer solicitud a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
datos = requests.get(url).json()['data']
#print (datos)

# Obtener la cantidad de empleados
num_empleados = len(datos)

# Calcular el promedio de salario de los empleados
salarios = [empleado['employee_salary'] for empleado in datos]
promedio_salario = sum(salarios) / len(salarios)
# Calcular el promedio de edad de los empleados
edades = [empleado['employee_age'] for empleado in datos]
promedio_edad = sum(edades) / len(edades)
# Calcular el salario mínimo y máximo
salario_minimo = min(salarios)
salario_maximo = max(salarios)
# Calcular la edad menor y mayor
edad_minima = min(edades)
edad_maxima = max(edades)


# Mostrar resultados
print(f"Cantidad de empleados: {num_empleados}")
print(f"Promedio de salario: {promedio_salario}")
print(f"Promedio de edad: {promedio_edad}")
print(f"Salario mínimo: {salario_minimo}")
print(f"Salario máximo: {salario_maximo}")
print(f"Edad menor: {edad_minima}")
print(f"Edad mayor: {edad_maxima}")