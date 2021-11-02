import csv

# Abrir archivo y lector
archivo = open('00-datos.csv')
lector_csv = csv.reader(archivo)

# leer encabezados
encabezados = next(lector_csv)
print('Encabezado: ' + str(encabezados))

#Leer Fila

for fila in lector_csv:
    print('Nombre: {0}, Apellido: {1}, email {2} '.format(fila[0], fila[1], fila[2]))

# Cerrar Archivo
archivo.close()