import time

def lavar_ropa(tipo_ropa):
    print(f"Lavando {tipo_ropa}...")
    time.sleep(4)  # Simula el tiempo de lavado
    print(f"{tipo_ropa} lavada.")

inicio = time.perf_counter()

tandadas = [
    "Ropa Blanca",
    "Ropa de Color",
    "Ropa Delicada"
]

for ropa in tandadas:
    lavar_ropa(ropa)

fin = time.perf_counter()
print(f"Tiempo total de lavado: {fin - inicio:.2f} segundos")
