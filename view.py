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

def getManagerCompany(username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getManagerCompany = "select comname from employee where username=%s";
			cursor.execute(getManagerCompany, (username))
			result = cursor.fetchone()
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

def getTheaterNames():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getTheaterNames = "select distinct thname from theater;";
			cursor.execute(getTheaterNames)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result	

def checkTheaterExists(company, theaterName):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			checkTheaterExists = "select thname from theater where comname=%s and thname=%s"
			cursor.execute(checkTheaterExists, (company, theaterName))
			result = cursor.fetchall()
	finally:
		connection.close()
	return result		

def getTheaterCapacity(theater):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getTheaterCapacity = "select capacity from theater where thname=%s;"
			cursor.execute(getTheaterCapacity, (theater))
			result = cursor.fetchone()
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

def getUnemployedManagers(company):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getUnemployedManagers = "select username, firstname, lastname from users where" \
			 + " username in (select username from employee where comname=%s AND thname IS NULL);"
			cursor.execute(getUnemployedManagers, (company))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def findMangerTheater(username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			findMangerTheater = "select thname from employee where username=%s"
			cursor.execute(findMangerTheater, (username))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result

def checkMovieExists(name, date):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			checkMovieExists = "select * from movie where movname=%s and movreleasedate=%s"
			cursor.execute(checkMovieExists, (name, date))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result

def getTheaterMovies(theater):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getTheaterMovies = """select * 
				from (select movname, movreleasedate, movplaydate from movieplay where thname=%s) T1 
				JOIN (select movname, movreleasedate, duration from movie) T2 
					on T1.movname=T2.movname AND T1.movreleasedate=T2.movreleasedate """
			cursor.execute(getTheaterMovies, (theater))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getTheaterMoviesFiltered(theater):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getTheaterMoviesFiltered = """select movname, movreleasedate, duration from movie
				where movname not in(select movname from movieplay where thname=%s);"""
			cursor.execute(getTheaterMoviesFiltered, (theater))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getAllMovies():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getAllMovies = """select * from movie"""
			cursor.execute(getAllMovies)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getAllPlayingMovies():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getAllPlayingMovies = """select distinct movname from movieplay"""
			cursor.execute(getAllPlayingMovies)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result	


def getTheaterMovieCount(theater, date):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getTheaterMovieCount = """select count(*) from movieplay where 
				thname=%s AND movplaydate=%s;"""
			cursor.execute(getTheaterMovieCount, (theater, date))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result


def getExploreMovieData():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:

			getExploreMovieData = """select T2.movname, T2.thname, T1.thstreet, T1.thcity, T1.thstate, T1.thzipcode,
			 T2.comname, T2.movplaydate from
			 (select thname, comname, thstreet, thcity, thstate, thzipcode from theater) T1
			 JOIN (select thname, comname, movplaydate, movname from movieplay) T2 
			 	on T1.thname=T2.thname AND T1.comname=T2.comname"""

			cursor.execute(getExploreMovieData)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result




def getviewHistory(username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			viewHistory = """select T2.movname, T2.thname, T2.comname, T2.creditcardnum, T2.movplaydate
				 from (select creditcardnum from customercreditcard where username=%s) T1
				 JOIN (select movname, thname, comname, creditcardnum, movplaydate from customerviewmovie) T2
				  on T1.creditcardnum=T2.creditcardnum"""
			cursor.execute(viewHistory, (username))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getVisitHistory(username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getVisitHistory = """select T1.thname, T2.thstreet, T1.comname, T1.visitdate from
			 (select thname, comname, visitdate from uservisittheater where username=%s) T1
			  JOIN 
			  (select thname, comname, thstreet from theater) T2
			   on T1.thname=T2.thname AND T1.comname=T2.comname"""
			cursor.execute(getVisitHistory, (username))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result



def getUserCreditCards(username):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getUserCreditCards = "select creditcardnum from customercreditcard where username=%s"
			cursor.execute(getUserCreditCards, (username))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

def getNumMoviesWatched(date):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getNumMoviesWatched = """select count(*) as cnt from
			(select * from customerviewmovie) T1
			  JOIN
			(select * from customercreditcard) T2
			 on T1.creditcardnum = T2.creditcardnum where movplaydate=%s;"""
			cursor.execute(getNumMoviesWatched, (date))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result

def getMovieReleaseDate(name):
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getMovieReleaseDate = "select movreleasedate from movie where movname=%s"
			cursor.execute(getMovieReleaseDate, (name))
			result = cursor.fetchone()
	finally:
		connection.close()

	return result


def getManagers():
	connection = util.db_connection()
	try:
		with connection.cursor() as cursor:
			getManagers = "select username from employee where employeetype=%s"
			cursor.execute(getManagers, ("Manager"))
			result = cursor.fetchall()
	finally:
		connection.close()

	return result