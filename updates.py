import util

def statusChange(usernames, typeStatus):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			if typeStatus == "Approve":
				statusChange = 'UPDATE users set status = IF(status = "Pending" or status =' \
				+' "Declined", "Approved", status) where username=%s'
			if typeStatus == "Decline":
				statusChange = 'UPDATE users set status = IF(status = "Pending",' \
				+ '"Declined", status) where username=%s'
			for username in usernames:
				cursor.execute(statusChange, (username))
			connection.commit()
	finally:
		connection.close()

	return True

def createMovie(name, date, duration):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			createMovie = "INSERT into movie values (%s, %s, %s)"
			cursor.execute(createMovie, (name, date, duration))
			connection.commit()
	finally:
		connection.close()

	return True	

def scheduleMovie(name, releaseDate, playDate, theater, company):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			scheduleMovie = "INSERT into movieplay values (%s, %s, %s, %s, %s)"
			cursor.execute(scheduleMovie, (name, releaseDate, playDate, theater, company))
			connection.commit()
	finally:
		connection.close()

	return True
	
def logTheaterVisits(visitTheaters, visitDate, username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			logTheaterVisits = "INSERT INTO uservisittheater (thname, comname, visitdate, username)" \
			+ "VALUES (%s, %s, %s, %s);"
			for theater, company in visitTheaters:
				cursor.execute(logTheaterVisits, (theater, company, visitDate, username))
			connection.commit()
	finally:
		connection.close()
	return True

def createTheater(company, theater, capacity, address, city, state, zipcode):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			createTheater = "INSERT INTO theater VALUES (%s, %s, %s, %s, %s, %s, %s);"
			cursor.execute(createTheater, (company, theater, capacity, address, city, state, zipcode))
			connection.commit()
	finally:
		connection.close()

	return True

def assignManager(theater, username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			createTheater = "UPDATE employee set thname=%s where username=%s;"
			cursor.execute(createTheater, (theater, username))
			connection.commit()
	finally:
		connection.close()

	return True

def watchMovie(movname, movreleasedate, movplaydate, thname, comname, creditcardnum):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			watchMovie = "INSERT INTO customerviewmovie values (%s, %s, %s, %s, %s, %s)"
			cursor.execute(watchMovie, (movname, movreleasedate, movplaydate, thname, comname, creditcardnum))
			connection.commit()
	finally:
		connection.close()

	return True


