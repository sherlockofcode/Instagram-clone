import sqlite3 as sql

def create():
	try:
		with sql.connect('database.db') as con:
			con.execute('''CREATE TABLE users (
					Id INTEGER PRIMARY KEY AUTOINCREMENT,
					Username TEXT NOT NULL,
					FirstName TEXT NOT NULL,
					LastName TEXT NOT NULL,
					Password CHAR(50) NOT NULL);''')
	except:
		print "table not created"

def addUser(request):
	error=0
	msg="Succesful"
	print "z"
#	try:
	print "ia"
	username = request.args['user']
	print "ia"
	password = request.args['pass']
	first = request.args['name1']
	last = request.args['name2']
	
	print "a"
	with sql.connect('database.db') as con:
		cur=con.cursor()
		print "b"
		query = "SELECT Username FROM users WHERE Username = ?"
		print "b"
		cur.execute(query,(username,))
		print "b"
		row = cur.fetchone()
		print "b"
		if row:
			msg="User already exists : try again with other username"
			error=1
		else:
			print "c"
			cur.execute("INSERT INTO users ( Username,FirstName,LastName,Password) VALUES (?,?,?,?)",(username,first,last,password))
			con.commit()
	return (msg,error)
#	except:
#		msg="Unexpected Error during insertion:try again"
#		error=1
#		return (msg,error)

