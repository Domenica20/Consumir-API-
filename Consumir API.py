import requests

# Hacer solicitud a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)
data = response.json()['data']

# Inicializar variables para cálculos
num_empleados = len(data)
salarios = [float(emp['employee_salary']) for emp in data]
edades = [int(emp['employee_age']) for emp in data]

# Calcular estadísticas
promedio_salario = sum(salarios) / num_empleados
promedio_edad = sum(edades) / num_empleados
salario_minimo = min(salarios)
salario_maximo = max(salarios)
edad_minima = min(edades)
edad_maxima = max(edades)

# Mostrar resultados
print(f"Cantidad de empleados: {num_empleados}")
print(f"Promedio de salario: {promedio_salario}")
print(f"Promedio de edad: {promedio_edad}")
print(f"Salario mínimo: {salario_minimo}")
print(f"Salario máximo: {salario_maximo}")
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")
