from flask import Flask, render_template, session, url_for, redirect, flash, request
import os
import auth
import view
import updates

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
				companyData=companyData)


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
				companyData=companyData)

	'''
	inside Manage Company screen is:
		-> Create Theater -> methods=['POST', 'GET']
		-> Company Detail -> methods=['GET']
	'''


@app.route('/admin/managecompany/createtheater', methods=['POST', 'GET'])
def createTheater():
	return redirect(url_for('home'))


@app.route('/admin/createmovie', methods=['POST', 'GET'])
def createMovie():

	if request.method == "POST":
		#run query to check if movie already exists
		# if it does, flash screen with error
		# if not, add to db and go to home page
		print(request.form)

	return render_template("funcs/create_movie.html")


@app.route('/manager/theateroverview', methods=['GET'])
def theaterOverview():
	return redirect(url_for('home'))

@app.route('/manager/schedulemovie', methods=['POST', 'GET'])
def scheduleMovie():
	return redirect(url_for('home'))

@app.route('/customer/exploremovie', methods=['POST', 'GET'])
def exploreMovie():
	return redirect(url_for('home'))

@app.route('/customer/viewhistory', methods=['GET'])
def viewHistory():
	return redirect(url_for('home'))


@app.route('/user/exploretheater', methods=['POST', 'GET'])
def exploreTheater():

	theaterNames = []
	companyNames = []


	if request.method == "POST":
		print(request.form)
		theater_name = request.form.get("theaternamefilter")
		city = request.form.get("city")
		company = request.form.get("company")
		state = request.form.get("state")
		visitDate = request.form.get("Visit Date")
		
		redefinedTheaterData = []

		filtertheaterData = view.filter_theaterdata(theater_name, city, company, state)

		#TODO: Return filtered data

		#TODO: Log visits -> get the radio button data

		return render_template('funcs/explore_theater.html', theaters=redefinedTheaterData,
				theaterNames=theaterNames, companyNames=companyNames, session=session)



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

			if theater['thname'] not in theaterNames:
				theaterNames.append(theater['thname'])

			if theater['comname'] not in companyNames:
				companyNames.append(theater['comname'])

			redefinedTheaterData.append(d)

		return render_template('funcs/explore_theater.html', theaters=redefinedTheaterData,
				theaterNames=theaterNames, companyNames=companyNames, session=session)

@app.route('/user/visitHistory', methods=['GET'])
def visitHistory():
	return redirect(url_for('home'))
