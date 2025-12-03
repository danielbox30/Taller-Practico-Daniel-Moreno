sumatoria = 0

for i in range(1, 11):
    calificacion = float(input(f"Ingrese la calificación {i}: "))
    sumatoria += calificacion

promedio = sumatoria / 10

print("Sumatoria:", sumatoria)
print("Promedio:", promedio)
