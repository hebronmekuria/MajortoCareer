import sqlite3
import os
from GeminiCategorizer.categorizer import job_descriptions, GeminiCategorizer
import json

db_name = "trialgemini.db"
db_path = os.path.normpath(db_name)

def entry_exists(conn, description):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM jobs WHERE description = ?", (description,))
    count = cur.fetchone()[0]
    return count > 0

def tuple_creator(job_descriptions):
    """Create a list of tuples where:
       - 0th element: a boolean
       - 1st element: a list of majors
       - 2nd element: job description"""
    entries_to_add = []
    for job_description in job_descriptions:
        major_bool_tuple = GeminiCategorizer(job_description)
        if major_bool_tuple[0] and major_bool_tuple[1]:
            entries_to_add.append((major_bool_tuple[0], major_bool_tuple[1], job_description))
    return entries_to_add

def add_to_db(conn, lst):
    cur = conn.cursor()
    for boolean, major, description in lst:
        serialized_list = json.dumps(major) # Convert list to string
        cur.execute('''
            INSERT INTO jobs (link, major, description) VALUES (?, ?, ?)
        ''', (str(boolean), serialized_list, description))
    conn.commit()
    print("Entries added to the database.")
    
def view_db(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM jobs')
    rows = cur.fetchall()
    for row in rows:
        print("Here is the --->", row)
        
def view_column(conn, column):
    cur = conn.cursor()
    cur.execute(f'SELECT {column} FROM jobs')
    rows = cur.fetchall()
    for row in rows:
        print(row[0][:50])
        
        
if __name__ == "__main__":
    conn = sqlite3.connect(db_name)
    entries_to_add = tuple_creator(job_descriptions)
    for entry in entries_to_add:
        if not entry_exists(conn, entry[2]):
            add_to_db(conn, [entry])
            view_column(conn, "link")
    conn.close()

            
        