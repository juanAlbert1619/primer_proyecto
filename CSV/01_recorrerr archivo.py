import csv

archivo = open('00-datos.csv')
lector = csv.reader(archivo, delimiter =',')

#next(lector)
for fila in lector:
    nombre = fila[0]
    #self.tabla.setItem(fila,  0, QTableWidgetItem(nombre))
    apellido = fila[1]
    #self.tabla.setItem(fila,  0, QTableWidgetItem(apellido))
    email = fila[2]
    #self.tabla.setItem(fila,  0, QTableWidgetItem(email))
    print(fila[0], fila[1],fila[2])
    
archivo = open ('01a_datos_guardar.csv', 'w', newline ='')
escritor_csv = csv.writer(archivo, delimiter =',', quotechar = '"')

# Escribir los datos
escritor_csv.writerow(fila[0], fila[1],fila[2])
   
   