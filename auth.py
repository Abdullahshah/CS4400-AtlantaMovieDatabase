import util

def login_user(username, password):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			login_user = "SELECT * FROM users WHERE username=%s and password=MD5(%s)"
			cursor.execute(login_user, (username, password))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result


def get_typeEmployee(username):
	connection = util.db_connection()

	try:
		with connection.cursor() as cursor:
			get_typeEmployee = "SELECT employeetype FROM employee WHERE username=%s"
			cursor.execute(get_typeEmployee, (username))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result

# Registration -----------------------------------------------------

def createNewUser(username, firstname, lastname, password, usertype, status):
	connection = util.db_connection()

	try:
		with connection.cursor() as cursor:
			createNewUser = "INSERT INTO users values (%s, %s, %s, MD5(%s), %s, %s)"
			cursor.execute(createNewUser, (username, firstname, lastname, password, usertype, status))
			connection.commit()
	finally:
		connection.close()

	return True

def createNewCustomer(username, firstname, lastname, password, usertype, status, creditCards):
	connection = util.db_connection()

	try:
		with connection.cursor() as cursor:
			createNewCustomer = "INSERT INTO users values (%s, %s, %s, MD5(%s), %s, %s)"
			cursor.execute(createNewCustomer, (username, firstname, lastname, password, usertype, status))

			addNewCreditCard = "INSERT INTO customercreditcard values (%s, %s)"
			for cc in creditCards:
				cursor.execute(addNewCreditCard, (username, cc))

			connection.commit()
	finally:
		connection.close()

	return True


def createNewManager(username, firstname, lastname, password, usertype, status, company, address_street,
		address_city, address_state, address_zip, theaterName="NULL"):

	connection = util.db_connection()

	try:
		with connection.cursor() as cursor:
			createNewManager = "INSERT INTO users values (%s, %s, %s, MD5(%s), %s, %s)"
			cursor.execute(createNewManager, (username, firstname, lastname, password, usertype, status))

			cursor.execute("SET foreign_key_checks = 0")
			addNewEmployee = "INSERT INTO employee values (%s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(addNewEmployee, (username, address_street, address_city, address_state,
							address_zip, "Manager", company, theaterName))
			cursor.execute("SET foreign_key_checks = 1")
			connection.commit()
	finally:
		connection.close()

	return True


def createNewManagerCustomer(username, firstname, lastname, password, usertype, status, company, address_street,
		address_city, address_state, address_zip, creditCards, theaterName="NULL"):

	connection = util.db_connection()

	try:
		with connection.cursor() as cursor:
			createNewManager = "INSERT INTO users values (%s, %s, %s, MD5(%s), %s, %s)"
			cursor.execute(createNewManager, (username, firstname, lastname, password, usertype, status))

			cursor.execute("SET foreign_key_checks = 0")
			addNewEmployee = "INSERT INTO employee values (%s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(addNewEmployee, (username, address_street, address_city, address_state,
							address_zip, "Manager", company, theaterName))
			cursor.execute("SET foreign_key_checks = 1")

			addNewCreditCard = "INSERT INTO customercreditcard values (%s, %s)"
			for cc in creditCards:
				cursor.execute(addNewCreditCard, (username, cc))

			connection.commit()
	finally:
		connection.close()

	return True