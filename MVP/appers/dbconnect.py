def insert_email(email):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into temp_emails values('{0}')".format(email)
		cursor.execute(sql)
		connection.commit()
	connection.close()