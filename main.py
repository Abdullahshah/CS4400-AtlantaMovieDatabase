from flask import Flask, render_template, session, url_for, redirect, flash, request
import os
import auth
import view
import updates
import datetime

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
	if 'usertype' not in session:
		print("usertype not in session. Current Session: ", session)
		return redirect(url_for('login'))

	function_screens = {
		"Admin Only": ["Manage User", "Explore Theater", "Manage Company", "Visit History", "Create Movie", "Sign Out"],
		"Admin-Customer": ["Manage User", "Explore Movie", "Manage Company", "Explore Theater", "Create Movie", "View History", "Visit History", "Sign Out"],
		"Manager Only": ["Theater Overview", "Explore Theater", "Schedule Movie", "Visit History", "Sign Out"],
		"Manager-Customer": ["Theater Overview", "Explore Movie", "Schedule Movie", "Explore Theater", "View History", "Visit History", "Sign Out"],
		"Customer": ["Explore Movie", "View History", "Explore Theater", "Visit History", "Sign Out"],
		"User": ["Explore Theater", "Visit History", "Sign Out"]
	}


	userType = session['usertype']
	return render_template("home.html", userType=userType, functions=function_screens[userType])


@app.route('/login', methods=['POST', 'GET'])
def login():
	#handle sign in and flash if incorrect user/pass creds
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		user_data_response = auth.login_user(username, password)
		if user_data_response:
			user_data = {k: v for d in user_data_response for k, v in d.items()}
			print("Successfuly Signed in with user data:", user_data)
			session['user_data'] = user_data

			if 'Employee' in user_data['usertype']:
				redefined_userType = ''
				if user_data['usertype'] == "Employee":
					employeeType = auth.get_typeEmployee(username)
					redefined_userType = employeeType['employeetype'] + " Only"
				else:
					employeeType = auth.get_typeEmployee(username)
					print("employeeType:", employeeType)
					redefined_userType = employeeType['employeetype'] + "-Customer"
				session['usertype'] = redefined_userType
			else: # usertype is "User" or "Customer"
				session['usertype'] = user_data['usertype']

			return redirect(url_for('home'))
		else:
			flash("Invalid email or password")

		return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'GET':
		return render_template('register.html', session=session)

	if request.method == 'POST':
		# print(request.form)
		if 'user_only' in request.form:
			print('user_only selected. Heading to user_registration.html')
			return render_template('regs/user_registration.html', session=session)
		elif 'customer_only' in request.form:
			print('customer_only selected. Heading to customer_only_registration.html')
			return render_template('regs/customer_only_registration.html', session=session)
		elif 'manager_only' in request.form:
			print('manager_only selected. Heading to manager_only_registration.html')
			return render_template('regs/manager_only_registration.html', session=session)
		else:
			print('manager_customer selected. Heading to manager_customer_registration.html')
			return render_template('regs/manager_customer_registration.html', session=session)
		return render_template('register.html', session=session)

@app.route('/register_forwarding', methods=['POST'])
def handle_registration():
	print(request.form)
	reg_type = request.form.get("registration_type") #type of registration
	print("registration type:", request.form.get("registration_type"))

	reg_types = {'User': 'regs/user_registration.html',
				 'Customer': 'regs/customer_only_registration.html',
				 "Manager Only": 'regs/manager_only_registration.html'}

	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")

	username = request.form.get("username")

	password = request.form.get('password')
	password_confirm = request.form.get('password_confirm')
	if password != password_confirm:
		flash("Entered passwords do not match")
		return render_template(reg_types[reg_type], session=session)

	if reg_type == "User":
		status = "Pending"
		if auth.createNewUser(username, first_name, last_name, password, reg_type, status):
			print("User created!")
	elif reg_type == "Customer":
		status = "Pending"
		creditCards = request.form.getlist("creditcard")
		if auth.createNewCustomer(username, first_name, last_name, password, reg_type, status, creditCards):
			print("Customer created!")
	elif reg_type == "Manager Only":
		usertype = "Employee"
		status = "Approved"
		company = request.form.get("company")
		address_street = request.form.get("address_street")
		address_city = request.form.get("address_city")
		address_state = request.form.get("address_state")
		address_zip = request.form.get("address_zip")

		if auth.createNewManager(username, first_name, last_name, password, usertype, status, company,
			 address_street, address_city, address_state, address_zip, theaterName="NULL"):
			print("Manager created!")
	else:
		usertype = "Employee, Customer"
		status = "Approved"
		company = request.form.get("company")
		address_street = request.form.get("address_street")
		address_city = request.form.get("address_city")
		address_state = request.form.get("address_state")
		address_zip = request.form.get("address_zip")

		creditCards = request.form.getlist("creditcard")

		if auth.createNewManagerCustomer(username, first_name, last_name, password, usertype, status, company, address_street,
		address_city, address_state, address_zip, creditCards, theaterName="NULL"):
			print("Manager-Customer created!")

	# after registration works
	session['usertype'] = reg_type

	user_data_response = auth.login_user(username, password)
	if user_data_response:
		user_data = {k: v for d in user_data_response for k, v in d.items()}
		print("Successfuly Signed in with user data:", user_data)
		session['user_data'] = user_data

	return redirect(url_for('home'))

@app.route('/functionality_forwarding', methods=['POST'])
def handle_functionality():
	print(request.form)
	function = request.form.get('function')
	print('function:', function)

	function_dict = {
		"Sign Out": "logout",
		#admin -----
		"Manage User": "manageUser",
		"Manage Company": "manageCompany", #createTheater, #companyDetail
		"Create Movie": "createMovie",
		#manager ----
		"Theater Overview": "theaterOverview",
		"Schedule Movie": "scheduleMovie",

		#customer ---
		"Explore Movie": "exploreMovie",
		"View History": "viewHistory",

		#user ---
		"Explore Theater": "exploreTheater",
		"Visit History": "visitHistory",
	}

	return redirect(url_for(function_dict[function]))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))


@app.route('/admin/manageuser', methods=['POST', 'GET'])
def manageUser():

	ccnum = {}
	queryData = view.creditCardCount()
	for item in queryData:
		ccnum[item['username']] = item['cnt']

	managersList = [x['username'] for x in view.getManagers()]
	print("managersList", managersList)

	if request.method == "GET":
		allUserData = view.getAllUserData()
		manageUserData = []
		for user in allUserData:
			userDict = {}
			userDict['username'] = user['username']

			if user['username'] in ccnum:
				userDict['ccc'] = ccnum[user['username']] #ccc = credit card count
			else:
				userDict['ccc'] = 0

			userDict['usertype'] = user['usertype']
			if "Employee" in userDict['usertype']:
				if userDict['username'] in managersList:
					userDict['usertype'] = userDict['usertype'].replace("Employee", "Manager")
				else:
					userDict['usertype'] = userDict['usertype'].replace("Employee", "Admin")

			userDict['status'] = user['status']
			manageUserData.append(userDict)

	if request.method == "POST":
		print(request.form)

		if request.form.get("approveDeclineButtons"):
			typeStatus = request.form.get("approveDeclineButtons")
			usernames = request.form.getlist("userChoice")
			updates.statusChange(usernames, typeStatus)
			print(typeStatus, "on users:", usernames)
		usernameFilter = request.form.get("username")
		statusFilter = request.form.get("status")

		allUserData = view.getAllUserData()
		manageUserData = []
		for user in allUserData:
			if usernameFilter != "" and usernameFilter != user['username']:
				continue
			userDict = {}
			userDict['username'] = user['username']

			if user['username'] in ccnum:
				userDict['ccc'] = ccnum[user['username']] #ccc = credit card count
			else:
				userDict['ccc'] = 0

			userDict['usertype'] = user['usertype']
			if "Employee" in userDict['usertype']:
				if userDict['username'] in managersList:
					userDict['usertype'] = userDict['usertype'].replace("Employee", "Manager")
				else:
					userDict['usertype'] = userDict['usertype'].replace("Employee", "Admin")

			if statusFilter != "All" and statusFilter != user['status']:
				continue
			userDict['status'] = user['status']

			manageUserData.append(userDict)

	return render_template("funcs/manage_user.html", manageUserData=manageUserData)


@app.route('/admin/managecompany', methods=['POST', 'GET'])
def manageCompany():
	
	companyNames = view.getCompanyNames()

	if request.method == "POST":

		print(request.form)

		if request.form.get("createTheaterButton"):
			print("createTheaterButton", "pressed")
			return redirect(url_for("createTheater"))

		if request.form.get("companyDetailButton"):
			companyChoice = request.form.get("companyChoice")
			if companyChoice:
				print("companyDetailButton", "pressed")
				managerNames = ''
				managerNameData = view.getManagersforCompany(companyChoice)
				for manager in managerNameData:
					managerNames += manager['firstname'] + ' ' + manager['lastname'] + ', '
				managerNames = managerNames[:-2]

				theaterData = []
				theaterQueryData = view.getWorkingManagersforCompany(companyChoice)
				for theater in theaterQueryData:
					theaterDict = {}
					theaterDict['name'] = theater['thname']
					theaterDict['manager'] = theater['firstname'] + ' ' + theater['lastname']
					theaterDict['city'] = theater['thcity']
					theaterDict['state'] = theater['thstate']
					theaterDict['capacity'] = theater['capacity']
					theaterData.append(theaterDict)
				print(theaterData)

				return render_template("funcs/company_detail.html", company=companyChoice,
						managerNames=managerNames, theaterData=theaterData)
			else:
				flash("Please select a company to view its details")


		cityMin = request.form.get("CityCoveredMin")
		cityMax = request.form.get("CityCoveredMax")
		theaterMin = request.form.get("NumTheatersMin")
		theaterMax = request.form.get("NumTheatersMax")
		employeeMin = request.form.get("NumEmployeesMin")
		employeeMax = request.form.get("NumEmployeesMax")

		queryData = view.manageCompanyGET()
		companyData = []

		for company in queryData:

			if cityMin != '' and int(cityMin) > company['numCities']:
				continue
			if cityMax != '' and int(cityMax) < company['numCities']:
				continue
			if theaterMin != '' and int(theaterMin) > company['numTheaters']:
				continue
			if theaterMax != '' and int(theaterMax) < company['numTheaters']:
				continue
			if employeeMin != '' and int(employeeMin) > company['numEmployees']:
				continue
			if employeeMax != '' and int(employeeMax) < company['numEmployees']:
				continue			

			companyDict = {}
			companyDict['name'] = company['comname']
			companyDict['numCities'] = company['numCities']
			companyDict['numTheaters'] = company['numTheaters']
			companyDict['numEmployees'] = company['numEmployees']
			companyData.append(companyDict)
		

		return render_template("funcs/manage_company.html", companyNames=companyNames,
				companyData=companyData, session=session)


	if request.method == "GET":
		queryData = view.manageCompanyGET()
		companyData = []

		for company in queryData:
			companyDict = {}
			companyDict['name'] = company['comname']
			companyDict['numCities'] = company['numCities']
			companyDict['numTheaters'] = company['numTheaters']
			companyDict['numEmployees'] = company['numEmployees']
			companyData.append(companyDict)
		

		return render_template("funcs/manage_company.html", companyNames=companyNames,
				companyData=companyData, session=session)

	'''
	inside Manage Company screen is:
		-> Create Theater -> methods=['POST', 'GET']
		-> Company Detail -> methods=['GET']
	'''


@app.route('/admin/managecompany/createtheater', methods=['POST', 'GET'])
def createTheater():

	if request.method == "POST":
		print(request.form)
		pageData = request.form
		if request.form.get("loadManagersButton"):
			print("loadManagersButton")
			company = request.form.get("companyName")

			queryData = view.getUnemployedManagers(company)
			managers = []
			for manager in queryData:
				managerDict = {}
				managerDict['username'] = manager['username']
				managerDict['name'] = manager['firstname'] + ' ' + manager['lastname']
				managers.append(managerDict)

			if managers == []:
				flash("No managers for this company!")

			return render_template("funcs/create_theater.html", pageData=pageData,
				session=session, companyNames=[{"comname":company}], managers=managers)


		if request.form.get("createTheaterButton"):
			companyName = request.form.get("companyName")
			theaterName = request.form.get("manageCompanytheaterName")
			theaterCapacity = request.form.get("theaterCapacity")
			theaterAddress = request.form.get("theaterAddress")
			theaterCity = request.form.get("theaterCity")
			theaterState = request.form.get("theaterState")
			theaterZIP = request.form.get("theaterZIP")
			manager = request.form.get("selectedManager")
			if view.checkTheaterExists(companyName, theaterName):
				flash("Theater already exists within company")
			else:
				if updates.createTheater(companyName, theaterName, theaterCapacity,
					theaterAddress, theaterCity, theaterState, theaterZIP):
					print("Theater Created!")
				if updates.assignManager(theaterName, manager):
					print("Manager Assigned!")
				return redirect(url_for("manageCompany"))

	pageData = {'theaterName': '',
	 'theaterAddress': '',
	 'theaterCity': '',
	 'theaterState': '',
	 'theaterZIP': '',
	 'theaterCapacity': ''}
	return render_template("funcs/create_theater.html", session=session,
		 pageData=pageData, companyNames=view.getCompanyNames())


@app.route('/admin/createmovie', methods=['POST', 'GET'])
def createMovie():

	if request.method == "POST":
		print(request.form)
		#run query to check if movie already exists
		# if it does, flash screen with error
		# if not, add to db and go to home page
		movieName = request.form.get("movieName")
		movieDuration = request.form.get("movieDuration")
		movieReleaseDate = request.form.get("movieReleaseDate")
		if not view.checkMovieExists(movieName, movieReleaseDate): #does not exist
			if updates.createMovie(movieName, movieReleaseDate, movieDuration):
				print("Movie Created!")
		else: #movie already exists
			flash("Movie already exists!")


	return render_template("funcs/create_movie.html")


@app.route('/manager/theateroverview', methods=['POST', 'GET'])
def theaterOverview():

	# 1)find name of theater they manage
	# select thname from employee where username=%s;

	# 2) if option not selected select * from (select movname, movreleasedate, movplaydate from movieplay where thname='Cinema Star') T1 JOIN (select movname, movreleasedate, duration from movie) T2 on T1.movname=T2.movname AND T1.movreleasedate=T2.movreleasedate;
	# 3) if option selected 
# select movname, movreleasedate, duration from movie 
# where movname not in 
# (select movname from movieplay where thname =%s);
	
	username = session['user_data']['username']
	theater = view.findMangerTheater(username)['thname']

	if request.method == "POST":
		print(request.form)

		filterName = request.form.get("movieName")
		durationMin = request.form.get("movieDurationMin")
		durationMax = request.form.get("movieDurationMax")
		releaseStart = request.form.get("movieReleaseStart")
		releaseEnd = request.form.get("movieReleaseEnd")
		playStart = request.form.get("moviePlayStart")
		playEnd = request.form.get("moviePlayEnd")


		movieData = []

		if theater:
			filtered = False
			movieQuery = []
			if request.form.get("played-notplayedFilter") == "NotPlayedFilter":
				movieQuery = view.getTheaterMoviesFiltered(theater)
				filtered = True
			else:
				movieQuery = view.getTheaterMovies(theater)

			for movie in movieQuery:
				movieDict = {}

				if filterName != '' and filterName not in movie['movname']:
					continue
				if durationMin != '' and int(durationMin) > movie['duration']:
					continue
				if durationMax != '' and int(durationMax) < movie['duration']:
					continue
				if releaseStart != '' and \
					datetime.datetime.strptime(releaseStart, '%Y-%m-%d').date() > movie['movreleasedate']:
					continue
				if releaseEnd != '' and \
					datetime.datetime.strptime(releaseEnd, '%Y-%m-%d').date() < movie['movreleasedate']:
					continue
				if playStart != '' and \
					datetime.datetime.strptime(playStart, '%Y-%m-%d').date() > movie['movplaydate']:
					continue
				if playEnd != '' and \
					datetime.datetime.strptime(playEnd, '%Y-%m-%d').date() < movie['movplaydate']:
					continue

				movieDict['name'] = movie['movname']
				movieDict['duration'] = movie['duration']
				movieDict['releaseDate'] = movie['movreleasedate']
				if not filtered:
					movieDict['playDate'] = movie['movplaydate']
				movieData.append(movieDict)


		return render_template("funcs/theater_overview.html", movieData=movieData)



	if request.method == "GET":
		# print(theater)
		movieData = []

		if theater:
			movieQuery = view.getTheaterMovies(theater)
			for movie in movieQuery:
				movieDict = {}
				movieDict['name'] = movie['movname']
				movieDict['duration'] = movie['duration']
				movieDict['releaseDate'] = movie['movreleasedate']
				movieDict['playDate'] = movie['movplaydate']
				movieData.append(movieDict)


		return render_template("funcs/theater_overview.html", movieData=movieData)



@app.route('/manager/schedulemovie', methods=['POST', 'GET'])
def scheduleMovie():
# find capacity of theater: select capacity from theater where thname='Cinema Star';
# find current amount on playDate: select count(*) from movieplay where thname='Cinema Star' AND movplaydate=' 2019-12-20';

# check if current amount < capacity:

#“Capacity” of a theater is the maximum number of movies it can play for the same date

	movieData = view.getAllMovies()
	for x in movieData:
		x['movieDisplayName'] = x['movname'] + ' - ' + x['movreleasedate'].strftime('%Y-%m-%d')

	if request.method == "POST":
		print(request.form)
		selectedMovieName = request.form.get("scheduledMovie")
		selectedPlayDate = request.form.get("scheduledPlayDate")

		scheduledReleasedDate = ''

		for x in movieData:
			if x['movname'] == selectedMovieName:
				scheduledReleasedDate = x['movreleasedate']

		if datetime.datetime.strptime(selectedPlayDate, '%Y-%m-%d').date() <=  scheduledReleasedDate:
			flash("Can not schedule movie before release date")
		else:
			print(session['user_data'])
			username = session['user_data']['username']
			theater = view.findMangerTheater(username)['thname']
			companyName = view.getManagerCompany(username)['comname']
			if not theater:
				flash("You do not belong to a theater")
			else:
				theaterCapacity = view.getTheaterCapacity(theater)['capacity']
				theaterMovieCount = view.getTheaterMovieCount(theater, selectedPlayDate)['count(*)']
				print("theaterCapacity:", theaterCapacity)
				print("theaterMovieCount:", theaterMovieCount)

				if theaterMovieCount == theaterCapacity:
					flash("Max Capacity of Scheduled Movies Reached")
				else:
					if updates.scheduleMovie(selectedMovieName, scheduledReleasedDate, selectedPlayDate, theater, companyName):
						print("Movie Scheduled!")


	return render_template("funcs/schedule_movie.html", movieData=movieData)

@app.route('/customer/exploremovie', methods=['POST', 'GET'])
def exploreMovie():

	# print(view.getExploreMovieData())

	query_data = view.getExploreMovieData()

	username = session['user_data']['username']
	creditCards = view.getUserCreditCards(username)

	movieData = []

	if request.method == "POST":
		print(request.form)

		if request.form.get("watchMovieButton"):
			moviesToWatch = request.form.getlist("movieChoice")
			if moviesToWatch:
				creditcard = request.form.get("creditCard")
				if creditcard != '---':
					print("movies selected:", moviesToWatch)
					for movieInfo in moviesToWatch:
						# print(eval(movieInfo))
						movie, movieDate, theater, company = eval(movieInfo)
						movieDate = movieDate.strftime('%Y-%m-%d')
						watchCount = view.getNumMoviesWatched(movieDate)['cnt']
						if watchCount == 3:
							flash("You've already seen three movies on this day: " + str(movieDate))
						else:
							movreleasedate = view.getMovieReleaseDate(movie)['movreleasedate']
							if updates.watchMovie(movie, movreleasedate, movieDate, theater, company, creditcard):
								print("Movie Watched!")
				else:
					flash("Please select a credit card")
			else:
				flash("Please Select a movie")


		movieName = request.form.get("movienamefilter")
		city = request.form.get("city")
		company = request.form.get("company")
		state = request.form.get("state")
		playStart = request.form.get("playDateMin")
		playEnd = request.form.get("playDateMax")

		for movie in query_data:
			m = {}

			if movieName != 'All' and movieName != movie['movname']:
				continue
			if city != '' and city != movie['thcity']:
				continue
			if company != 'All' and company != movie['comname']:
				continue
			if state != 'All' and state != movie['thstate']:
				continue
			if playStart != '' and \
				datetime.datetime.strptime(playStart, '%Y-%m-%d').date() > movie['movplaydate']:
				continue
			if playEnd != '' and \
				datetime.datetime.strptime(playEnd, '%Y-%m-%d').date() < movie['movplaydate']:
				continue

			m['name'] = movie['movname']
			m['theater'] = movie['thname']
			m['address'] = movie['thstreet'] + ', ' + movie['thcity'] + ', ' \
				+ movie['thstate'] + ' ' + str(movie['thzipcode'])
			m['company'] = movie['comname']
			m['playdate'] = movie['movplaydate']

			movieData.append(m)

	if request.method == "GET":
		for movie in query_data:
					m = {}
					m['name'] = movie['movname']
					m['theater'] = movie['thname']
					m['address'] = movie['thstreet'] + ', ' + movie['thcity'] + ', ' \
						+ movie['thstate'] + ' ' + str(movie['thzipcode'])
					m['company'] = movie['comname']
					m['playdate'] = movie['movplaydate']

					movieData.append(m)


	return render_template("funcs/explore_movie.html", companyNames=view.getCompanyNames(),
			allMovies=view.getAllPlayingMovies(), movieData=movieData, ccData=creditCards)


@app.route('/customer/viewhistory', methods=['GET'])
def viewHistory():
	username = session['user_data']['username']
	userViewData = view.getviewHistory(username)
	return render_template('funcs/view_history.html', viewData = userViewData)


@app.route('/user/exploretheater', methods=['POST', 'GET'])
def exploreTheater():

	if request.method == "POST":
		print(request.form)
		theater_name = request.form.get("theaternamefilter")
		city = request.form.get("city")
		company = request.form.get("company")
		state = request.form.get("state")

		#if log visit button is pressed
		if request.form.get("logVisitButton"):
			visitDate = request.form.get("Visit Date")
			visitTheaters = request.form.getlist("theaterChoice")
			if visitDate == '':
				flash("Please enter a date to log a visit")
				if not visitTheaters:
					flash("Please select theaters to visit")
			elif not visitTheaters:
				flash("Please select theaters to visit")
			else:
				visitTheaters = [eval(x) for x in visitTheaters]
				print(visitTheaters)
				username = session['user_data']['username']
				if updates.logTheaterVisits(visitTheaters, visitDate, username):
					print("Logged Visits!")
		
		theaterData = view.get_theaterdata()

		redefinedTheaterData = []

		for theater in theaterData:
			d = {}

			if theater_name != 'All' and theater_name != theater['thname']:
				continue
			if city != '' and city != theater['thcity']:
				continue
			if company != 'All' and company != theater['comname']:
				print("comname:", theater['comname'])
				continue
			if state != 'All' and state != theater['thstate']:
				continue

			d['Theater'] = theater['thname']
			d['Address'] = theater['thstreet'] + ', ' + theater['thcity'] + ', ' \
				+ theater['thstate'] + ' ' + str(theater['thzipcode'])
			d['Company'] = theater['comname']

			redefinedTheaterData.append(d)

		return render_template('funcs/explore_theater.html', theaters=redefinedTheaterData,
				theaterNames=view.getTheaterNames(), companyNames=view.getCompanyNames())



	if request.method == "GET":
		theaterData = view.get_theaterdata()

		print(theaterData)

		redefinedTheaterData = []

		for theater in theaterData:
			d = {}
			d['Theater'] = theater['thname']
			d['Address'] = theater['thstreet'] + ', ' + theater['thcity'] + ', ' \
				+ theater['thstate'] + ' ' + str(theater['thzipcode'])
			d['Company'] = theater['comname']

			redefinedTheaterData.append(d)

		return render_template('funcs/explore_theater.html', theaters=redefinedTheaterData,
				theaterNames=view.getTheaterNames(), companyNames=view.getCompanyNames())

@app.route('/user/visitHistory', methods=['POST', 'GET'])
def visitHistory():
	username = session['user_data']['username']
	queryData = view.getVisitHistory(username)
	viewData = queryData

	if request.method == "POST":
		print(request.form)
		visitDateMin = request.form.get("visitDateMin")
		visitDateMax = request.form.get("visitDateMax")
		company = request.form.get("company")
		
		viewData = []
		for viewx in queryData:
			if visitDateMin != '' and \
				datetime.datetime.strptime(visitDateMin, '%Y-%m-%d').date() > viewx['visitdate']:
				continue
			if visitDateMax != '' and \
				datetime.datetime.strptime(visitDateMax, '%Y-%m-%d').date() < viewx['visitdate']:
				continue
			if company != 'All' and company != viewx['comname']:
				continue

			viewData.append(viewx)

	return render_template("funcs/visit_history.html", viewData=viewData, companyNames=view.getCompanyNames())
