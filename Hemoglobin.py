import json

# Secuencia de aminoácidos
secuencia = "MVHLTPEEKSAVTALWGKVNVDEVGGEALG"

# Mostrar información básica
print("Proteína: Hemoglobina beta humana")
print("Secuencia:", secuencia)
print("Longitud:", len(secuencia), "aminoácidos")

# Lista de aminoácidos posibles
aminoacidos = "ACDEFGHIKLMNPQRSTVWY"

# Contar cada aminoácido
conteo = {}

for aa in aminoacidos:
    conteo[aa] = secuencia.count(aa)

print("\nConteo de aminoácidos:")
for aa, cantidad in conteo.items():
    print(aa, ":", cantidad)

# Pesos moleculares aproximados
pesos = {
"A":89.09,"C":121.15,"D":133.10,"E":147.13,"F":165.19,
"G":75.07,"H":155.16,"I":131.17,"K":146.19,"L":131.17,
"M":149.21,"N":132.12,"P":115.13,"Q":146.15,"R":174.20,
"S":105.09,"T":119.12,"V":117.15,"W":204.23,"Y":181.19
}

# Calcular peso molecular
peso_total = 0

for aa in secuencia:
    peso_total += pesos[aa]

print("\nPeso molecular aproximado:", round(peso_total,2),"Da")

# Aminoácidos hidrofóbicos
hidrofobicos = ["A","V","I","L","M","F","W","Y"]

contador_hidro = 0

for aa in secuencia:
    if aa in hidrofobicos:
        contador_hidro += 1

porcentaje_hidro = (contador_hidro / len(secuencia)) * 100

print("Porcentaje hidrofóbico:", round(porcentaje_hidro,2),"%")

# Crear diccionario con resultados
resultados = {
"proteina": "Hemoglobina beta humana",
"secuencia": secuencia,
"longitud": len(secuencia),
"peso_molecular": round(peso_total,2),
"porcentaje_hidrofobico": round(porcentaje_hidro,2),
"conteo_aminoacidos": conteo
}

# Guardar archivo JSON
with open("resultados_hemoglobina.json","w") as archivo:
    json.dump(resultados, archivo, indent=4)

print("\nArchivo JSON generado correctamente")