import json
import sqlite3
from flask import Blueprint, jsonify, request
from flask_cors import CORS

bp = Blueprint('jobs', __name__)
CORS(bp)  # Enable CORS for this blueprint

def create_database():
    try:
        cntn = sqlite3.connect('jobs.db')
    except sqlite3.Error as e:
        print(e)
    finally:
        if cntn:
            cntn.close()

def create_test_table():
    try:
        connection = sqlite3.connect('jobs.db')
        query = '''CREATE TABLE IF NOT EXISTS jobstest(
                      Url TEXT PRIMARY KEY, 
                      Job_Title TEXT, 
                      Major TEXT, 
                      Location TEXT, 
                      Pay TEXT, 
                      Skills TEXT, 
                      Description TEXT)
                      '''
        
        connection.execute(query)
    except sqlite3.Error as e:
        pass
    finally:
        if connection:
            connection.close()

def alter_table():
    try:
        connection = sqlite3.connect('jobs.db')
        query = ''' ALTER TABLE jobstest 
        ADD Date TEXT'''

        connection.execute(query)
    except sqlite3.Error as e:
        pass
    finally:
        if connection:
            connection.close()

#this function will be triggered after our incoming data gets refreshed
def clean_up_table():
    try:
        connection = sqlite3.connect('jobs.db')
        query = ''' DELETE FROM jobstest;'''
        connection.execute(query)
        populate_test_table()  #populate with new data

    except sqlite3.Error as e:
        pass
    finally:
        if connection:
            connection.close()

def populate_test_table():
    with open('/Users/hebronmekuria/MajortoCareer/backend/testdata.json', 'r') as file:  # Adjust the path as necessary
        data = json.load(file)
    try:
        connection = sqlite3.connect('jobs.db')
        cursor = connection.cursor()
        for job in data:
            try:
                cursor.execute('''INSERT INTO jobstest 
                                  (URL, Job_Title, Major, Location, Pay, Skills, Description, DATE) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?,?)''', 
                               (job['URL'], job['Job Title'], job['College Major'], job['Location'], 
                                job['Pay'], ', '.join(job['Skills Required']), job['Description'], job['Date']))
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

@bp.route('/findjobs', methods=['POST'])
def query_test_table():
    alter_table()
    major = request.headers.get('Major')
    if not major:
        return jsonify({"error": "Major header is required"}), 400

    populate_test_table()
    try:
        connection = sqlite3.connect('jobs.db')
        cursor = connection.execute('SELECT * FROM jobstest WHERE Major = ? ORDER BY Date ASC', (major,))
        res = []
        for row in cursor:
            res.append({
                'url': row[0],
                'jobtitle': row[1],
                'major': row[2],
                'location': row[3],
                'pay': row[4],
                'skills': row[5],
                'desc': row[6]
            })
        print(res)
        return jsonify(res)
    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()
