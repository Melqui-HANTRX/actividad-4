registro_estudiante = {}

def agregar_estudiante():
 nombre = input("ingrese el nombre del estudiante:").strip()
 if nombre in registro_estudiante:
   print(f"(el estudiante '{nombre}' ya esta registrado con calificaciones {registro_estudiante}")
   retur
