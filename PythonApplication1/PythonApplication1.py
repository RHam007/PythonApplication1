
# Using python to create db

# Library import
import sqlite3
import os
from unicodedata import category
# Create/Configure Database
#  - name
DATABASE_PATH = 'school.db'

# - connection path
connection = sqlite3.connect(DATABASE_PATH)

# - active connection variable
cursor = connection.cursor()

# - Table 1 creation ('companies'), variables are lower_cased, options/operators are all CAPS

sql = (
    '''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    '''
    )

# - execute SQL command(s)
cursor.execute(sql)

# - Table 2 creation ('courses'), variables are lower_cased, options/operators are all CAPS
sql = (
    '''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            company_id INTEGER
        )
    '''
    
    )
# - execute SQL command(s)
cursor.execute(sql)


# Insert record into db
# Note: Each execution of the sql commits will append the same value to the table each time.
# So multiple executions of the first SQL commit will add multiple "Mammoth Interactive" to the table with a new id number
# To reset, delete the "schools.db" file (it'll be recreated on next script run)

# - Create variable to call SQL to add the 'name' to the 'companies' table
sql = "INSERT INTO companies (name) VALUES(?)"

# - Executing the SQL with the 'name' variable defined (no "id" value required as the 'id' field autoincrements)
cursor.execute(sql,("Mammoth Interactive",))

# - commit change(s)
connection.commit()

# - to add additional values
cursor.execute(sql,("Bura Tech",))

# - and commit change(s)
connection.commit()

# - Insert record to additional table(s)
sql = "INSERT INTO courses (name, category, company_id) VALUES (?,?,?)"

# - Pass all parameter values into table
cursor.execute(sql,("Hello Coding", "programming", 1))

# - commit changes
connection.commit()

# Query the db (SELECT FROM WHERE)

# - Find the number of companies in the 'companies' table
companies = connection.execute("SELECT count(id) FROM companies").fetchone()

print(*companies)

# - Find the number of courses in the 'courses' table
courses = connection.execute("SELECT count(id) FROM courses").fetchone()

print(*courses)

# - Return first id of a course named "Hello coding"
cursor.execute("SELECT id FROM courses WHERE name=?", ("Hello Coding",))
print(cursor.fetchone())

# - Return first id of a course named "Machine Learning" [hint: there is none]
cursor.execute("SELECT id FROM courses WHERE name=?", ("Machine Learning",))
print(cursor.fetchone())

# - Return first id of a company named "Mammoth Interactive"
cursor.execute("SELECT id FROM companies WHERE name=?", ("Mammoth Interactive",))
print(cursor.fetchone())

# - Add a new record for a course named "Complete Machine Learning"
sql = "INSERT INTO courses (name, category, company_id) VALUES (?,?,?)"
cursor.execute(sql,("Complete Machine Learning", "programming", 1))

# - Return all of the id's for courses with catergory "programming"
cursor.execute("SELECT id FROM courses WHERE category=?", ("programming",))
print(cursor.fetchall())

# - Return all of the names for courses with catergory "programming"
cursor.execute("SELECT name FROM courses WHERE category=?", ("programming",))
print(cursor.fetchall())

# - debugging for db thread timeouts [results in db locked error]
#cursor.close()

# Connecting to database (added library 'os')
def connect(path="school.db", syncdb=False):
    # - Check database exists
    if os.path.exists(path):
        connection = sqlite3.connect(path, timeout=5.0)

    # Create the database if it doesn't already exist
    else:
        syncdb = True
    

    return connection

# adding new row

# - Promting user for course name, category, and company
print("Enter Course name: ")
name = input()

print("Enter course category: ")
category = input()

print("Enter course company id: ")
company_id = input()

# - Defining function to insert values to a new row
def insert_row_into_courses(name, category, company_id, connection):
    sql = "INSERT INTO courses (name, category, company_id) VALUES (?,?,?)"
    cursor = connection.cursor()
    cursor.execute(sql, (name, category, company_id))
    connection.commit()
    

# - Execution
insert_row_into_courses(name, category, company_id, connect())