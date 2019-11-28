import pymysql.cursors
import os
# Connect to the database

def db_connection():
    # return pymysql.connect(host=os.getenv('DB_HOST'),
    #                        user=os.getenv('DB_USER'),
    #                        password=os.getenv('DB_PASSWD'),
    #                        db=os.getenv('DB_NAME'),
    #                        charset='utf8mb4',
    #                        cursorclass=pymysql.cursors.DictCursor)



    return pymysql.connect(host='localhost',
                           user='admin',
                           password='password',
                           db='team70',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
def get_company_names():
    connection = db_connection()
    try:
        with connection.cursor() as cursor:
            get_company_names = "select * from company;"
            cursor.execute(get_company_names)
            result = cursor.fetchall()
    finally:
        connection.close()

    return result