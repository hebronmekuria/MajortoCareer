import json
import requests
from bs4 import BeautifulSoup
import re

# Function to get job description
def get_job_description(url):
    # Fetch the job page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the job description
    description = soup.find('div', class_='description__text')
    if description:
        # Clean up the description
        cleaned_description = description.text.strip()
        cleaned_description = re.sub(r'\s+', ' ', cleaned_description)  # Replace multiple spaces/newlines with a single space
        cleaned_description = cleaned_description.replace("Show more", "").replace("Show less", "")
        return cleaned_description
    else:
        return "No description available"

def linkedin_scraper(webpage, major, known_links, job_data):
    encoded_major = major.replace(" ", "%20")
    page = 0
    jobs_found = True

    while jobs_found:
        url = webpage.format(encoded_major, page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card', limit=10)
        if not jobs:
            jobs_found = False  # Break the loop if no jobs are found
            continue

        for job in jobs:
            job_link = job.find('a', class_='base-card__full-link')['href']

            # Check for duplicates based on job links
            if job_link not in known_links:
                known_links.add(job_link)

                job_title = job.find('h3', class_='base-search-card__title').text.strip()
                job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
                job_location = job.find('span', class_='job-search-card__location').text.strip()
                job_description = get_job_description(job_link)

                job_data.append({
                    "title": job_title,
                    "company": job_company,
                    "location": job_location,
                    "apply_link": job_link,
                    "description": job_description
                })

        page += 10  # Increase the start parameter for the next page (assuming 10 jobs per page)

# Initialize a list to store job data
job_data = []

# Initialize a set to keep track of unique job titles
known_links = set()

# # List of majors
# majors = [
#         'Accounting', 'Actuarial Science', 'Advertising', 'Aerospace Engineering', 'Aeronautical Engineering',
#         'African American Studies', 'Agricultural Engineering', 'Agriculture', 'American Sign Language', 'American Studies',
#         'Animal Science', 'Anthropology', 'Apparel Design', 'Applied Mathematics', 'Aquatic Biology',
#         'Archaeology', 'Architecture', 'Art Education', 'Art History', 'Asian Studies',
#         'Astronomy', 'Biochemistry', 'Bioengineering', 'Biology', 'Biomedical Engineering',
#         'Biophysics', 'Biotechnology', 'Business Administration', 'Business Analytics', 'Chemical Engineering',
#         'Chemical Physics', 'Chemistry', 'Child Development', 'Chinese Language and Literature', 'Civil Engineering',
#         'Classical Studies', 'Clinical Psychology', 'Cognitive Science', 'Communication', 'Communications Disorders',
#         'Comparative Literature', 'Computer Engineering', 'Computer Science', 'Construction Engineering', 'Construction Management',
#         'Counseling', 'Creative Arts', 'Creative Writing', 'Criminal Justice', 'Criminology',
#         'Culinary Arts', 'Cybersecurity', 'Dance', 'Data Science', 'Dental Hygiene',
#         'Dietetics', 'Digital Media', 'Dramatic Arts', 'Early Childhood Education', 'Earth and Space Science',
#         'Earth Science', 'Ecology', 'Economics', 'Education', 'Educational Leadership',
#         'Electrical Engineering', 'Elementary Education', 'Engineering', 'Engineering Physics', 'Engineering Technology',
#         'English', 'Entomology', 'Environmental Engineering', 'Environmental Health', 'Environmental Science',
#         'Epidemiology', 'Equine Studies', 'Ethnic Studies', 'Ethnomusicology', 'European Studies',
#         'Exercise Science', 'Family Studies', 'Fashion Design', 'Fashion Merchandising', 'Film and Television',
#         'Film Studies', 'Finance', 'Financial Planning', 'Fine Arts', 'Fire Science',
#         'Fisheries and Wildlife', 'Food Science', 'Forensic Science', 'Forestry', 'French Language and Literature',
#         'Game Design', 'Genetics', 'Geography', 'Geology', 'Geospatial Science',
#         'German Language and Literature', 'Graphic Design', 'Health Administration', 'Health Education', 'Health Information Management',
#         'Health Sciences', 'Historic Preservation', 'History', 'Horticulture', 'Hospitality Management',
#         'Human Biology', 'Human Development', 'Human Resources', 'Human Services', 'Industrial Design',
#         'Industrial Engineering', 'Information Science', 'Information Technology', 'Integrated Marketing Communications', 'Interior Design',
#         'International Business', 'International Relations', 'Italian Language and Literature', 'Japanese Language and Literature', 'Jewish Studies',
#         'Journalism', 'Kinesiology', 'Landscape Architecture', 'Landscape Design', 'Latin American Studies',
#         'Law Enforcement', 'Legal Studies', 'Liberal Arts', 'Library Science', 'Linguistics',
#         'Management', 'Manufacturing Engineering', 'Marketing', 'Marine Biology', 'Materials Science',
#         'Mathematical Economics', 'Mathematics', 'Mechanical Engineering', 'Media Production', 'Media Studies',
#         'Medical Laboratory Science', 'Microbiology', 'Middle Eastern Studies', 'Military Science', 'Molecular Biology',
#         'Music', 'Music Education', 'Music Performance', 'Museum Studies', 'Nanotechnology',
#         'Neuroscience', 'Nuclear Engineering', 'Nursing', 'Nutrition', 'Occupational Health',
#         'Occupational Therapy', 'Oceanography', 'Operations Management', 'Optometry', 'Organizational Leadership',
#         'Paleontology', 'Parks and Recreation', 'Pharmaceutical Sciences', 'Pharmacy', 'Philosophy',
#         'Photography', 'Physical Education', 'Physical Therapy', 'Physics', 'Plant Science',
#         'Political Science', 'Pre-Dentistry', 'Pre-Law', 'Pre-Medicine', 'Pre-Veterinary Medicine',
#         'Psychology', 'Public Administration', 'Public Health', 'Public Policy', 'Public Relations',
#         'Radio and Television', 'Radiologic Technology', 'Real Estate', 'Recreation and Leisure Studies', 'Religious Studies',
#         'Renewable Energy', 'Respiratory Therapy', 'Robotics', 'Russian Language and Literature', 'Science Education',
#         'Social and Behavioral Sciences', 'Social Work', 'Sociology', 'Software Engineering', 'Soil Science',
#         'Spanish Language and Literature', 'Special Education', 'Speech Pathology', 'Sport Management', 'Statistics',
#         'Supply Chain Management', 'Sustainable Agriculture', 'Systems Engineering', 'Telecommunications', 'Theatre',
#         'Theology', 'Therapeutic Recreation', 'Toxicology', 'Transportation and Logistics', 'Urban Planning',
#         'Veterinary Medicine', 'Veterinary Technology', 'Video Game Design', 'Visual Arts', 'Viticulture and Enology',
#         'Water Resources', 'Wildlife Biology', 'Wildlife Management', 'Women\'s Studies', 'Zoology'
#     ]

# for major in majors:
#     linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={}&start={}', major, known_titles, job_data)
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={}&start={}', "Biology", known_links, job_data)   

print('Scraping completed.')

# Write job data to a JSON file
with open('linkedin-jobs.json', 'w', encoding='utf-8') as file:
    json.dump(job_data, file, indent=4)

print('Job data saved to linkedin-jobs.json')