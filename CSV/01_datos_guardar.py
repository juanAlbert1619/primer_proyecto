import csv

#Abrir archivos y escritor

archivo = open ('01_datos_guardar.csv', 'w', newline ='')
escritor_csv = csv.writer(archivo, delimiter =',', quotechar = '"')

# Escribir los datos
escritor_csv.writerow(['Jose', 'Sanchez', 'js@gmail.com'])
escritor_csv.writerow(['Maria', 'Lopes', 'marl@gmail.com'])
escritor_csv.writerow(['Soledad', 'Busto', 'sb@gmail.com'])

# Cerrar archivo

archivo.close


