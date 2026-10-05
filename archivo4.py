nombres = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")
lista_notas = []
cantidad = int(input("Dime la cantidad de notas que desea ingresar: "))

for nota in range(cantidad):
    nota = float(input(f"Dime la nota {nota + 1}: "))
    lista_notas.append(nota)

promedio = sum(lista_notas) / len(lista_notas)
maxima = max(lista_notas)
minima = min(lista_notas)

datos = f"Nombre: {nombres.title()}\nApellidos: {apellidos.title()}\nNotas: {', '.join([str(nota) for nota in lista_notas])}\nPromedio: {promedio}\nMáxima: {maxima}\nMínima: {minima}"

with open("estudiante.txt", "w", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado satisfactoriamente")