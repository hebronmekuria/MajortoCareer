import sqlite3
import os
from GeminiCategorizer.categorizer import job_descriptions, GeminiCategorizer
import json



db_path = "backend/jobs.db"
db_path = os.path.normpath(db_path)



conn = sqlite3.connect(db_path)

cur = conn.cursor()

""" a list of tuples where:
0th element - a boolean
1st element - a list of majors
2nd element - job description """
list_to_add_to_db = [
    
] 

for job_description in job_descriptions:
    major_bool_tuple = GeminiCategorizer(job_description)
    if major_bool_tuple[0] == True and major_bool_tuple[1]:
        list_to_add_to_db.append((major_bool_tuple[0], major_bool_tuple[1], job_description))
        
print (list_to_add_to_db)
        

count = 0
for boolean, major, description in list_to_add_to_db:
    count += 1
    serialized_list = json.dumps(major) # converts list to string to use as a single entry in db, need to deserialize using json.loads to use as a list again
    cur.execute('''
            INSERT INTO jobstest (Link, Skills, Description) VALUES (?, ?, ?)
        ''', (str(boolean) + str(count) , serialized_list, description))

conn.commit()

# to see whats in database
cur.execute('SELECT * FROM jobstest')
rows = cur.fetchall()
for row in rows:
    print("this is", row)
    
conn.close()