registro = []
cant = int(input("¿Cuántos estudiantes registrarás? "))

for i in range(cant):
    nombre = input(f"\nEscribe el nombre del {i+1} estudiante: ")
    apellido = input(f"El apellido del {i+1} estudiante: ")
    nota = float(input(f"Dime la nota del {i+1} estudiante: "))
    
    registro.append([nombre, apellido, nota])

if registro:
    notas = [estudiante[2] for estudiante in registro]
    nota_mas_alta = max(notas)
    nota_mas_baja = min(notas)
    
    print()
    print(f"Nota más alta: {nota_mas_alta}")
    print(f"Nota más baja: {nota_mas_baja}")
    print()
    
    estudiantes_ordenados = sorted(registro, key=lambda x: x[2], reverse=True)
    
    top_3 = estudiantes_ordenados[:3]
    
    print("\nTOP 3 ESTUDIANTES CON MEJOR NOTA")
    for pos, est in enumerate(top_3, 1):
        print(f"{pos}º Lugar: {est[0]} {est[1]} - Nota: {est[2]}")
else:
    print("No se registraron estudiantes.")