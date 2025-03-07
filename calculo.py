def calcular_disponibilidad(minutos_inactivos, dias_mes=30):
    minutos_totales = dias_mes * 24 * 60  # Total de minutos en el mes
    disponibilidad = ((minutos_totales - minutos_inactivos) / minutos_totales) * 100
    return round(disponibilidad, 2)

# Ejemplo de uso
minutos_inactivos = 240 # Cambia esto por el tiempo real de inactividad
disponibilidad = calcular_disponibilidad(minutos_inactivos)
print(f"Disponibilidad mensual: {disponibilidad}%")