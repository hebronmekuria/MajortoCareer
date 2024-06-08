import sqlite3

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
        query='CREATE TABLE jobstest( Link TEXT PRIMARY KEY, JOBTITLE TEXT, LOCATION TEXT, PAY TEXT, Skills Text, Description TEXT)'
        connection.execute(query)
    except sqlite3.Error as e:
        pass
    finally:
        if connection:
            connection.close()

def populate_test_table():
    try:
        connection = sqlite3.connect('jobs.db')
        connection.execute ("INSERT INTO jobstest VALUES ('linkedin.com','software engineer','New York, NY','198,000 annual','Python, Java, SQL','This job will be remote')")
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()    

def query_test_table():
    try:
        connection = sqlite3.connect('jobs.db')
        cursor = connection.execute('SELECT * FROM jobstest')
        for row in cursor:
            print(row)
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()    



create_database()
create_test_table()
populate_test_table()
query_test_table()