from flask import Flask, render_template, session, url_for, redirect, flash, request
import os
import auth

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
	if 'usertype' not in session:
		# print("user_type:", session['user_type'])
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
			session['usertype'] = user_data['usertype']
			session['user_data'] = user_data
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
	user_type = request.form.get("registration_type")
	print(request.form.get("registration_type"))


	print("Credit Cards:", request.form.getlist("creditcard"))

	reg_types = {'User': 'regs/user_registration.html'}

	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")

	username = request.form.get("username")

	password = request.form.get('password')
	password_confirm = request.form.get('password_confirm')
	if password != password_confirm:
		flash("Entered passwords do not match")
		return render_template(reg_types[user_type], session=session)

	# TODO: Run SQL Query to register user


	# after registration works
	session['user_type'] = user_type

	return redirect(url_for('home'))

@app.route('/functionality_forwarding', methods=['POST'])
def handle_functionality():
	print(request.form)
	function = request.form.get('function')
	print('function:', function)

	function_dict = {
		"Sign Out": "logout",
		#admin -----
		"Manage User": "managerUser",
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
	return redirect(url_for('home'))


@app.route('/admin/managecompany', methods=['GET'])
def manageCompany():
	return redirect(url_for('home'))

	'''
	inside Manage Company screen is:
		-> Create Theater -> methods=['POST', 'GET']
		-> Company Detail -> methods=['GET']
	'''

@app.route('/admin/managecompany/createtheater', methods=['POST', 'GET'])
def createTheater():
	return redirect(url_for('home'))


@app.route('/admin/managecompany/companydetail', methods=['GET'])
def companyDetail():
	return redirect(url_for('home'))

@app.route('/admin/createmovie', methods=['POST', 'GET'])
def createMovie():
	return redirect(url_for('home'))


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
	return redirect(url_for('home'))

@app.route('/user/visitHistory', methods=['GET'])
def visitHistory():
	return redirect(url_for('home'))