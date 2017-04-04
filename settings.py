import psycopg2

#+-----------------------------------------------------+#
#|                  DATABASE SETTING                   +#
#+-----------------------------------------------------+#
# Noted that this database port is 5432

DATABASE_NAME = 'YOUR_DATABASE_NAME'
DATABASE_USER = 'YOUR_USER'
DATABASE_HOST = 'YOUR_DATABASE_HOST'
DATABASE_PASSWORD = 'YOUR_PASSWORD'
DATABASE_STRING_FORM = "postgresql://{}:{}@{}:5432/{}"
DATABASE_STRING = DATABASE_STRING_FORM.format(DATABASE_USER, DATABASE_PASSWORD,
                                              DATABASE_HOST, DATABASE_NAME)

def getDatabaseString():
    return DATABASE_STRING
