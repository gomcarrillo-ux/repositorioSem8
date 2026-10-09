listas = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola"]
print(listas)

conjuntos = {1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola"}
print(conjuntos)

tuplas = (1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola")
print(tuplas)

diccionarios = {"Estudiante": "Juanito", "Sexo": "Diario", "Nota": 85}
print(diccionarios)

diccionarios["Hola"]=80
print(diccionarios)

nuevaLista = []
nuevaLista.append(listas)
nuevaLista.append(conjuntos)
nuevaLista.append(tuplas)
nuevaLista.append(diccionarios)
print(nuevaLista)

for item in nuevaLista:
    print(item)


for item in nuevaLista:
    print(type(nuevaLista))

with open("texto.txt", "+a", encoding="utf-8") as archivo:
    for item in nuevaLista:
        archivo.write(str(item) + "\n")

with open("text.txt", "tw", encoding="utf-8") as archivo:
    for item in nuevaLista:
        archivo.write(str(item) + "\n")