import google.generativeai as genai
import os
from dotenv import load_dotenv
import ast #cool module that converts a list in string form to a list

### api security
load_dotenv()
api_key = os.getenv('API_KEY')
if api_key is None:
    raise ValueError("API_KEY env variable not set")


genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

### Mock Job Descriptions
job_description1 = '''Locations: VA - McLean, United States of America, McLean, VirginiaSenior Software Engineer (Python, AWS)cl

Senior Software Engineer, Back End

Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive, and iterative delivery environment? At Capital One, you'll be part of a big group of makers, breakers, doers and disruptors, who love to solve real problems and meet real customer needs. We are seeking Back End Software Engineers who are passionate about marrying data with emerging technologies. As a Capital One Software Engineer, you’ll have the opportunity to be on the forefront of driving a major transformation within Capital One.

What You’ll Do: 

 Collaborate with and across Agile teams to design, develop, test, implement, and support technical solutions in full-stack development tools and technologies 
 Share your passion for staying on top of tech trends, experimenting with and learning new technologies, participating in internal & external technology communities, mentoring other members of the engineering community 
 Collaborate with digital product managers, and deliver robust cloud-based solutions that drive powerful experiences to help millions of Americans achieve financial empowerment 
 Utilize programming languages like Java, Python, SQL, Node, Go, and Scala, Open Source RDBMS and NoSQL databases, Container Orchestration services including Docker and Kubernetes, and a variety of AWS tools and services 

Basic Qualifications: 

 Bachelor’s Degree 
 At least 4 years of professional software engineering experience (Internship experience does not apply) 

Preferred Qualifications:

 5+ years of experience in at least one of the following: Java, Scala, Python, Go, or Node.js 
 1+ years of experience with AWS, GCP, Azure, or another cloud service 
 3+ years of experience in open source frameworks 
 2+ years of experience in Agile practices 

At this time, Capital One will not sponsor a new applicant for employment authorization for this position.

The minimum and maximum full-time annual salaries for this role are listed below, by location. Please note that this salary information is solely for candidates hired to perform work within one of these locations, and refers to the amount Capital One is willing to pay at the time of this posting. Salaries for part-time roles will be prorated based upon the agreed upon number of hours to be regularly worked.

New York City (Hybrid On-Site): $165,100 - $188,500 for Senior Software Engineer

Candidates hired to work in other locations will be subject to the pay range associated with that location, and the actual annualized salary amount offered to any candidate at the time of hire will be reflected solely in the candidate’s offer letter.

This role is also eligible to earn performance based incentive compensation, which may include cash bonus(es) and/or long term incentives (LTI). Incentives could be discretionary or non discretionary depending on the plan.

Capital One offers a comprehensive, competitive, and inclusive set of health, financial and other benefits that support your total well-being. Learn more at the Capital One Careers website . Eligibility varies based on full or part-time status, exempt or non-exempt status, and management level.

This role is expected to accept applications for a minimum of 5 business days.No agencies please. Capital One is an equal opportunity employer committed to diversity and inclusion in the workplace. All qualified applicants will receive consideration for employment without regard to sex (including pregnancy, childbirth or related medical conditions), race, color, age, national origin, religion, disability, genetic information, marital status, sexual orientation, gender identity, gender reassignment, citizenship, immigration status, protected veteran status, or any other basis prohibited under applicable federal, state or local law. Capital One promotes a drug-free workplace. Capital One will consider for employment qualified applicants with a criminal history in a manner consistent with the requirements of applicable laws regarding criminal background inquiries, including, to the extent applicable, Article 23-A of the New York Correction Law; San Francisco, California Police Code Article 49, Sections 4901-4920; New York City’s Fair Chance Act; Philadelphia’s Fair Criminal Records Screening Act; and other applicable federal, state, and local laws and regulations regarding criminal background inquiries.

If you have visited our website in search of information on employment opportunities or to apply for a position, and you require an accommodation, please contact Capital One Recruiting at 1-800-304-9102 or via email at RecruitingAccommodation@capitalone.com . All information you provide will be kept confidential and will be used only to the extent required to provide needed reasonable accommodations.

For technical support or questions about Capital One's recruiting process, please send an email to Careers@capitalone.com

Capital One does not provide, endorse nor guarantee and is not liable for third-party products, services, educational tools or other information available through this site.

Capital One Financial is made up of several different entities. Please note that any position posted in Canada is for Capital One Canada, any position posted in the United Kingdom is for Capital One Europe and any position posted in the Philippines is for Capital One Philippines Service Corp. (COPSSC).'''

job_description2 = '''About the job
Are you a talented data engineer? Are you familiar with the needs of law offices? Take advantage of this rare chance to make your mark on a modernization project in e-discovery for a massive organization in Virginia! 



Due to a changing IT landscape, the preeminent law firm in Virginia is seeking an experienced Data Engineer to join the team in Richmond, VA. If you have data analysis experience and knowledge of Electronic Discovery Reference Models framework, apply today!



Some benefits for you:

Competitive compensation: starting up to $108,000!
Comprehensive benefits: Medical, dental, vision, 401(k) plus match and more
Impact: Get the exposure you deserve to senior leadership! In this role, you will be responsible for a modernization project that will change the face of our organization! This is a chance to make a lasting impact on how we do business and analyze records!
Stability: Tired of working contract jobs that have little chance of extending. Worry no more! This is a chance to join a premiere org in Virginia on direct hire!


What we need from you:

Bachelor’s degree in computer science, information systems, or a related field
3-5 years of experience in eDiscovery. Industry specific certifications is a plus.
Previous eDiscovery experience with a government legal department, law firm or vendor is preferred. 
Expertise in industry standard e-discovery tools and technologies
Strong verbal and written communication skills; ability to communicate effectively and clearly to both technical and non-technical staff.
Strong organizational and documentation skills with the ability to initiate, manage, and report tasks independently, as identified.
Working knowledge of litigation support technology including database applications (CS DISCO, Everlaw, Relativity).
Familiarity with system administration on MacOS, Microsoft Windows, and Linux / Unix operating systems as well as mobile device management (Android, iOS).
Ability to preserve confidentiality and exercise discretion.
Ability to work independently or as part of a cross functional team in a production
 environment.
Ability to work on multiple, simultaneous cases in a time-pressured environment where priorities are constantly changing.
Strong analytical and problem-solving skills while working under strict deadlines in a legal environment and the ability to interact with all levels of staff and attorneys.
Knowledge of the litigation process, from initial filing through trial, along with procedures related to e-discovery, including Federal Rules of Civil Procedure and the Electronic Discovery Reference Model (EDRM) for effective communication with legal teams.
Excellent attention to detail and ability to work independently and as part of a team.
Strong communication skills.
Knowledge of Everlaw and related certifications are a plus. '''

job_description3 = """About the job
Contract: 6+ months 

Hybrid: Chicago, IL (3 days on-site) 



The Change Management Lead is responsible for focusing on the people side of change, including changes to business processes, systems and technology, job roles and organization structures. They will work to drive faster adoption, higher ultimate utilization and greater proficiency of the changes that impact employees in the organization to increase benefit realization, value creation, ROI and the achievement of results and outcomes.




Tasks & Responsibilities:

• Consulting and coaching senior leaders and project team members regarding their roles in change management.
• Assessing and capturing change impacts, including recurring reviews of change impacts.
• Identifying the associated stakeholders impacted by the change impacts.
• Developing and executing a detailed change management plan (including communications, training, and engagement activities) for stakeholders to adopt the identified changes.
• Hosting, developing, and/or executing change management activities as defined in the change management plan, and as necessary to support adoption of the changes.
• Identifying, analyzing and preparing risk mitigation tactics to address behavioral change.
• Supporting the communication efforts (e.g., messaging, contributing to content creation) related to change management.
• Uses insights from change management assessments and progress of behavioral change during the course of the project as input into the communications.
• Developing and deploying in readiness assessments (e.g., communication plan has been executed, training has been delivered, appropriate level of competency has been demonstrated).
• Defining and measuring the success/adoption metrics and monitoring change progress, which may include executing pulse surveys and tracking attendance or viewership metrics.
• Reporting status up to the program level change management lead and participating in program change level activities.
• Manage the portfolio and change load to understand changes impacting the business areas from other initiatives.




Job Qualifications:

• Organizational Design
• Experience with Deposit Banking, preferred
- Experience with Teller implementations, preferred (FIS D1 Teller is an advantage)
• Change Management"""

### Main Code
prompt = f'''For the job description, {job_description3}, answer these questions in sequence:
1. Does the job description explicitly mention the requirement of a Bachelor's Degree? If yes, return True. If no, return False.
2. If True, what undergraduate major would be required? Return the distinct possible majors explicitily mentioned within the 'qualifications' section in the description in an array.
No explanation need, just answers, please.'''
response = model.generate_content(prompt)

#response.resolve() # sometimes helps when streaming answer
print(response.text) 


### Output Extraction

def GeminiAnnotator(response):
    # First split to separate answers separated by line
    split1 = response.text.split('\n')

    # Second splits to separate answer from numbers

    if len(split1) == 3:
        IsBachelor = ast.literal_eval(split1[0].split(". ")[1])
        MajorList = ast.literal_eval(split1[1].split(". ")[1])
    else:
        IsBachelor = ast.literal_eval("False")
        MajorList = ast.literal_eval('[]')


    
    #print("This is the length of the split", len(split1))
    #print(IsBachelor, MajorList)

    return (IsBachelor, MajorList)
