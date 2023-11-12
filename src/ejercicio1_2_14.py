numeroPayasos = int(input("Nº payasos: "))
numeroMuniecas = int(input("Nº muñecas: "))
pesoPayasos = 0.112
pesoMuniecas = 0.075

pesoTotal= (numeroPayasos*pesoPayasos) + (numeroMuniecas * pesoMuniecas)

print("El paquete a enviar pesará ", round(pesoTotal,3), " kg.")