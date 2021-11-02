import csv
# El módulo csv.reader toma los siguientes parámetros:
# with open ('00-datos.csv', newline = '') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# DictReader y DictWriter son clases disponibles en Python para leer y escribir a un CSV

# with open('00-datos.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_00-datos.csv'], row['last_00-datos.csv'])

# with open('S2-BAS - Fórmulas DESAFÍOS.csv') as file:
#     reader = csv.reader(file, delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
#     for row in reader:
#         print(row)


resultados = []
with open('00-datos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        resultados.append(row)
    print (resultados)

# Veamos ahora cómo escribir datos a un archivo CSV usando la función csv.writer y la clase csv.Dictwriter discutida al inicio de este tutorial.
# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]

# myFile = open('example2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)
    
# print("Writing complete")


# Escribiendo a un Archivo CSV Usando DictWriter
#Escribamos los siguientes datos a un CSV.

with open('example4.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})

print("Writing complete")