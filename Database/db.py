import mysql.connector

class database():
	def __init__(self, host, user, key, db):
		try:
			self.con = mysql.connector.connect(host = host, 
				user = user, password = key, database = db)
			if self.con.is_connected():
				print ("Conexion exitosa con base de datos '" + str(db)+"'")

		except ValueError as e:
			print "Error de conexion: \n"
			print e
		self.cur = self.con.cursor()
		

	def closedb(self):
		self.cur.close()
		self.con.close()
		print "Conexion finalizada"

	def insert(self, db, **kargs):
		query = "INSERT INTO %s (" % db
		keys = tuple(kargs.keys())
		values = tuple(kargs.values())
		l = len(kargs) - 1

		for i, key in enumerate(keys):
			query += ""+key+""
			if i < l:
				query += ", "
		query += ') VALUES %s' % str(values)

		print "Ejecutando insert: " + query + "\n"
		self.cur.execute(query)
		self.con.commit()
		print "guardado con exito"

	def printall(self, db):
		query = "SELECT * FROM %s" % db

		print "Ejecutando: " + query + "\n"
		self.cur.execute(query)

		filas = self.cur.fetchall()

		for i in filas:
			print i
		print "\n"

	def select(self, db, *args):
		query = "SELECT "
		l = len(args) - 1
		for i, arg in enumerate(args):
			query += ""+arg+""
			if i < l:
				query += ", "
		query += ' FROM %s' % db

		print "Ejecutando: " + query + "\n"

		self.cur.execute(query)

		filas = self.cur.fetchall()
		#columnas = len(self.cur.description)

		for i in filas:
			print i
		print "\n"

	def update(self, db,**kargs):
		query = "UPDATE %s SET " % db
		keys = kargs.keys()
		values = kargs.values()

		l = len(kargs)-2
		for i, karg in enumerate(kargs):
			if i == l:
				pass
			else:
				query += ""+keys[i]+"='"+values[i]+"'"
				if i < l:
					query += ", "

		query += " WHERE "+keys[l]+"='"+values[l]+"'"
		

		print "Ejecutando update: " + query + "\n"
		self.cur.execute(query)
		self.con.commit()
		print "guardado con exito"

	def delete(self, db,*args):
		query = "DELETE FROM %s WHERE" % db
		pass #en construccion

		#explora la posibilidad de agregar a las funciones 
		#un WHERE opcional
