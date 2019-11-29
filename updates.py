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









