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


def getCompanyNames():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getCompanyNames = "select * from company";
			cursor.execute(getCompanyNames)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result	

def manageCompanyGET():

	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			manageCompanyGET =	"""select * 
		from (select comname, count(distinct thcity) as numCities from theater group by comname) T1 
		JOIN (select comname, count(distinct thname) as numTheaters from theater group by comname) T2 
			on T1.comname = T2.comname 
		JOIN (select comname, count(employeetype) as numEmployees from employee group by comname) T3 
			on T1.comname = T3.comname;"""
			cursor.execute(manageCompanyGET)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result
'''
# City Covered
select comname, count(distinct thcity) from theater group by comname;

+-------------------------+------------------------+
| comname                 | count(distinct thcity) |
+-------------------------+------------------------+
| 4400 Theater Company    |                      3 |
| AI Theater Company      |                      1 |
| Awesome Theater Company |                      1 |
| EZ Theater Company      |                      2 |
+-------------------------+------------------------+



# Theaters
select comname, count(distinct thname) from theater group by comname;
+-------------------------+------------------------+
| comname                 | count(distinct thname) |
+-------------------------+------------------------+
| 4400 Theater Company    |                      3 |
| AI Theater Company      |                      1 |
| Awesome Theater Company |                      1 |
| EZ Theater Company      |                      2 |
+-------------------------+------------------------+
4 rows in set (0.00 sec)



#Employee
select comname, count(employeetype) from employee group by comname;
+-------------------------+---------------------+
| comname                 | count(employeetype) |
+-------------------------+---------------------+
| NULL                    |                   1 |
| 4400 Theater Company    |                   6 |
| AI Theater Company      |                   3 |
| Awesome Theater Company |                   2 |
| EZ Theater Company      |                   3 |
+-------------------------+---------------------+

'''

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


def getManagersforCompany(company):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getManagersforCompany = "select firstname, lastname from users" \
			+ " where username in (select username from employee where comname=%s)"
			cursor.execute(getManagersforCompany, (company))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getWorkingManagersforCompany(company):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getWorkingManagersforCompany = 	"""select *
			from (select username, comname, thname from employee where comname=%s) T1
			JOIN (select username, firstname, lastname from users) T2
			 on T1.username = T2.username
			JOIN (select comname, thname, thcity, thstate, capacity from theater) T3
			 on T1.thname = T3.thname AND T1.comname = T3.comname;"""
			cursor.execute(getWorkingManagersforCompany, (company))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result