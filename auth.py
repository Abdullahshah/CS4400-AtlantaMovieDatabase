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


def get_user(email, pw):
    connection = util.db_connection()

    try:
        with connection.cursor() as cursor:
            get_email = "SELECT user_id, email, name, suspended, is_admin FROM user WHERE email=%s and password=%s"
            cursor.execute(get_email, (email, pw))
            result = cursor.fetchone()
    finally:
        connection.close()

    return result