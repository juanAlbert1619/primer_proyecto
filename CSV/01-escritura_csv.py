import csv
# Abrir archivo y escritor

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

with open('metodo_escritura.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})

print("Writing complete")