import dotenv, os, psycopg

DB_CONN_STR='postgresql://neondb_owner:npg_XemR9YQf5juP@ep-crimson-thunder-ag25ghqr-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&options=endpoint%3Dep-crimson-thunder-ag25ghqr'

# # get conn str from file
# dotenv.load_dotenv()
# db_conn_str = os.getenv('DB_CONN_STR')

# with psycopg.connect(DB_CONN_STR) as conn: # establish connection to db
# 	with conn.cursor() as cur: # create cursor for query
# 		cur.execute('SELECT * FROM teacher;') # execute sql statement
# 		rows = cur.fetchall() # read results
# 		for row in rows: # traverse result rows
# 			print(row)
# 		conn.commit() # clean database structures used in query

# # ---------------------------------------------------------------------
# import dotenv, os, psycopg

dotenv.load_dotenv()
#db_conn_str = os.getenv('DB_CONN_STR')

with psycopg.connect(DB_CONN_STR) as conn:
	while True: # keep adding teachers
		# read data from user
		teacher_email = input('teacher email: ')
		name = input('name: ')
		# add to database, ensure persistence, recover from errors
		try:
			with conn.cursor() as cur:
				cur.execute('INSERT INTO teacher VALUES (%s, %s);', # each %s
							(teacher_email, name)) # ... from tuple
				conn.commit() # end transaction (persistence, clean-up)
		except Exception as e:
			print(e)
			conn.rollback() # reset; ignore changes after last commit

# # -----------------------------------------------------------------------
# # teachers and courses
# import dotenv, os, psycopg

# # model classes
# class Teacher:
# 	def __init__(self, teacher_email, name):
# 		self.teacher_email = teacher_email
# 		self.name = name
# 		self.courses = []

# 	# string representation showing email, name and courses
# 	def __str__(self):
# 		return f'{self.teacher_email} {self.name} [{" ".join([str(c) for c in self.courses])}]'

# class Course:
# 	def __init__(self, course_id, topic, teacher):
# 		self.course_id = course_id
# 		self.topic = topic
# 		self.teacher = teacher # note: "foreign key" as object reference

# 	# string representation showing email, name and email of teacher
# 	def __str__(self):
# 		return f'{self.course_id} {self.topic} {self.teacher.teacher_email}'

# courses = []
# dotenv.load_dotenv()
# db_conn_str = os.getenv('DB_CONN_STR')

# # read teachers, add one course for first teacher, construct objects
# with psycopg.connect(db_conn_str) as conn:
# 	# read teachers from db, store into list
# 	with conn.cursor() as cur:
# 		cur.execute("SELECT * FROM teacher;")
# 		rows = cur.fetchall()
# 		teachers = [Teacher(*row) for row in rows] # tuple unpacking for args

# 	# add one course for first teacher, store in db
# 	with conn.cursor() as cur:
# 		topic = 'integration'
# 		teacher = teachers[0]
# 		# following statement returns generated surrogate key
# 		cur.execute('INSERT INTO course (topic, teacher_email) VALUES (%s, %s) RETURNING course_id;',
# 					(topic, teacher.teacher_email))
# 		course_id = cur.fetchone()[0] # fetch generated synthetic key
# 		course = Course(course_id, topic, teacher)
# 		courses.append(course)
# 		teacher.courses.append(course)

# # print objects to see what we ended up with
# for t in teachers: print(t)
# for c in courses: print(c)
# # -----------------------------------------------------------------------
