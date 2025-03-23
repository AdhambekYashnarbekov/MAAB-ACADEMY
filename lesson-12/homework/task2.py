import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

db_file = "jobs.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        application_link TEXT,
        UNIQUE(job_title, company, location)
    )
''')
conn.commit()


url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_elements = soup.find_all("div", class_="card-content")

for job in job_elements:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="description").text.strip()
    application_link = job.find("a", class_="apply")['href'].strip()
    
   
    cursor.execute("SELECT description, application_link FROM jobs WHERE job_title=? AND company=? AND location=?", (title, company, location))
    existing_job = cursor.fetchone()
    
    if existing_job:
        if existing_job[0] != description or existing_job[1] != application_link:
            cursor.execute("""
                UPDATE jobs 
                SET description=?, application_link=? 
                WHERE job_title=? AND company=? AND location=?
            """, (description, application_link, title, company, location))
    else:
        cursor.execute("""
            INSERT INTO jobs (job_title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, application_link))

conn.commit()


def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)
    
    cursor.execute(query, params)
    return cursor.fetchall()


def export_jobs_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)

conn.close()

