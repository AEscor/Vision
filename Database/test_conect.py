import mysql.connector
import datetime
import sys, os

os.system ("cls")

con = mysql.connector.connect(host='localhost',user='root', password='ima1', database="test")
print "coneccion con la base de datos."
cursor = con.cursor()
raw_input()

pet = ('''SELECT nombre, origen, nacimiento FROM empleados;''')
cursor.execute(pet)

for (nombre, origen, nacimiento) in cursor:
	print ("{}, {}, {}".format(nombre, origen, nacimiento))

print "\nprueba de datos\n"
n = raw_input("Nombre: ")
o = raw_input("Origen: ")
a = input("Ano de nacimiento: ")
m = input("Mes de nacimiento: ")
d = input("Dia de nacimiento: ")

nac = datetime.date(a, m, d)
print nac

agregar = ('''INSERT INTO empleados VALUES (%s, %s, %s)''')

cursor.execute(agregar, (n, o, str(nac)))
#cursor.execute("INSERT INTO empleados VALUES ('pedro','polo','"+str(nac)+"')")
raw_input()

cursor.execute(pet)

for  (nombre, origen, nacimiento) in cursor:
	print ("{}, {}, {}".format(nombre, origen, nacimiento))

print "Guardar cambios?\n 's' Si 'n' No"
if raw_input() == "s":
	con.commit()
elif raw_input() == "n":
	pass
	
cursor.close()
con.close()	
print "\n Fin del programa."

