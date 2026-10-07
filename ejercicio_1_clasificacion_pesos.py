# Lista dada con los pesos de las piezas en kg
pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

# Contador de piezas aprobadas (ligeras y pesadas)
piezas_validas = 0

# Bucle para clasificar cada pieza según su peso
for peso in pesos_piezas:
    if peso <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif 1 <= peso <= 13:
            print("Pieza Ligera aprobada.")
            piezas_validas += 1
    elif peso > 13:
            print("Pieza Pesada aprobada.")
            piezas_validas += 1
# Muestra del total final de piezas válidas
print(f"Total de piezas válidas: {piezas_validas}")

