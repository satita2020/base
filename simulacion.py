import random

def simular_disponibilidad(dias=31, umbral_sla=98.9):
    minutos_totales = dias * 24 * 60 
    
    # Simular inactividad diaria aleatoria entre 0 y 30 min (puedes ajustarlo)
    tiempos_inactivos = [random.randint(0, 30) for _ in range(dias)]
    print(f"{tiempos_inactivos}")
    
    total_inactividad = sum(tiempos_inactivos)  # Total de minutos inactivos en 2 semanas
    
    # Calcular disponibilidad
    disponibilidad = ((minutos_totales - total_inactividad) / minutos_totales) * 100
    
    print(f"Total de minutos en 1 mes: {minutos_totales}")
    print(f"Minutos totales de inactividad: {total_inactividad}")
    print(f"Disponibilidad calculada: {disponibilidad:.2f}%")
    
    # Evaluar si cumple con el SLA
    if disponibilidad >= umbral_sla:
        print("✅ El sistema cumple con el SLA.")
    else:
        print("❌ El sistema NO cumple con el SLA.")

# Ejecutar simulación
simular_disponibilidad()
