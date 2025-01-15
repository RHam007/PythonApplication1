
# Library import
import sqlite3
import os
from unicodedata import category


# Connecting to database (added library 'os')
def connect(path="E:\Python\projects\PythonApplication1\PythonApplication1\school.db", syncdb=False):
    # - Check database exists
    if os.path.exists(path):
        connection = sqlite3.connect(path)

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
    
connection = connect()
# - Execution
insert_row_into_courses(name, category, company_id, connect())

courses_count = connection
