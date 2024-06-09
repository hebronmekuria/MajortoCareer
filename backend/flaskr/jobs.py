import json
import sqlite3
from flask import Blueprint, jsonify

bp = Blueprint('jobs', __name__)

# Create the connection to the db, if the db doesn't exist, it will be created and then the connection is created
def create_database():
    try:
        cntn = sqlite3.connect('jobs.db')
    except sqlite3.Error as e:
        print(e)
    finally:
        if cntn:
            cntn.close()

# Simple SQL query to create the test table
def create_test_table():
    try:
        connection = sqlite3.connect('jobs.db')
        query='CREATE TABLE IF NOT EXISTS jobstest( Url TEXT PRIMARY KEY, Job_Title TEXT, Major TEXT, Location TEXT, Pay TEXT, Skills Text, Description TEXT)'
        connection.execute(query)
    except sqlite3.Error as e:
        pass
    finally:
        if connection:
            connection.close()

# Populate test table using some mock json data in testdata.json
def populate_test_table():
    #Start by saving what's inside the json file
    with open('/Users/hebronmekuria/MajortoCareer/backend/testdata.json', 'r') as file:
        data = json.load(file)
    try:
        connection = sqlite3.connect('jobs.db')
        cursor = connection.cursor()
        for job in data:
            try:
                cursor.execute('''INSERT INTO jobstest 
                                  (URL, Job_Title, Major, Location, Pay, Skills, Description) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                               (job['URL'], job['Job Title'], job['College Major'], job['Location'], 
                                job['Pay'], ', '.join(job['Skills Required']), job['Description']))
                connection.commit()
            except sqlite3.IntegrityError as e:
                print(f"Data already exists for URL: {job['URL']}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

create_database()
create_test_table()
populate_test_table()

@bp.route('/findjobs', methods=['GET'])
def query_test_table():
    try:
        connection = sqlite3.connect('jobs.db')
        cursor = connection.execute('SELECT * FROM jobstest')
        res=[]
        for row in cursor:
            res.append(row)
        return jsonify(res)
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()   
