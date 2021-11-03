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