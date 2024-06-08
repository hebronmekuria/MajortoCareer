def add_jobs(conn, job):
    sql = ''' INSERT INTO jobstest(Link, Title, Pay, Location, Skills, Description)
    VALUES(?,?,?,?,?,?) ''' #initialize sql statement, but the ? are placeholders
    cur = conn.cursor() #initialize cursor
    cur.execute(sql,job) #execute sql statement
    conn.commit() #apply the change permanently by using commit
    return cur.lastrowid #return the inserted id


try:
    with sqlite3.connect("jobs.db") as conn:
        job = ('https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3939277796&eBP=CwEAAAGP6tQonSfjNcYtTf9i6e-DoRGU10tu5qjuTK-BDOhnIHxWgQsLw-GCvlp5n2yvoPU5APyci-j9wJDK3auowIEOOCPEtuEmIRntxJK6XBey60b8moM6AHR5LZyNBWEs6RD8GPBoYByjtz-8fcywRfk3RPULOWObX2_XoFYaOSeFci4G2S-TWtwg8l-cwXAdma2gvbYEbs7nNHA1cNKWd23nyPXwtKrRN25w9roLMb7japQd9MVtjn1hMsHwWuXXl_uwlKMNZ9FETUOpdTVx5RzHRXvLOZAKzg0xBr3QaoPZaqgSk7G3mgqtZJg5-dVJV6cavRpYhinNLi2YCwz-hPDIAUHyKm0c6jt7QFO4jW_PcyQTA9FGWn5-oyaf2L_YVdCfNl9Cz9Ux4V9s_ZB2-ke_W9igXGNL-9lv7N_BznJQvtQvZ-hpQSPbtoGuUqhj&refId=lc5qg9pt5j4xMamIZRT%2BJA%3D%3D&trackingId=RuslRVboH1odmeI2%2BXZ%2B2w%3D%3D',
       'Technical Support Engineer - Azure Cloud Security ',
       '67000','Washington, DC', 'Query Languages, Operating Systems', 'With over 18,000 employees worldwide, the Microsoft Customer Experience & Success (CE&S) organization is responsible for the strategy, design, and implementation of Microsoft’s end-to-end customer experience. Come join CE&S and help us build a future where customers come to us not only because we provide industry-leading products and services,')
        job_id=add_jobs(conn, job)
        print(job_id)
except sqlite3.Error as e:
    print(e)