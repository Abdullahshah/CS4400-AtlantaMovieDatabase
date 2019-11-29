import util




def getAllUserData():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getAllUserData = "select * from users;"
			cursor.execute(getAllUserData)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result


def creditCardCount():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			creditCardCount = "select username, count(*) as cnt" \
			 + " from customercreditcard group by username;"
			cursor.execute(creditCardCount)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result

def get_theaterdata():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			get_theaterdata = "select * from theater;"
			cursor.execute(get_theaterdata)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def filter_theaterdata(theater, city, company, state):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			get_theaterdata = "select * from theater where comname=%s and "
			cursor.execute(get_theaterdata)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result