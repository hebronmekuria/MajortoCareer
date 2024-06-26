from GeminiCategorizer.categorizer import *
from GeminiCategorizer.database_connector import *

import json
import os

import asyncio
import time
import google.api_core.exceptions
import aiosqlite 


#ADD LOGIC TO CHECK IF DESCRIPTION ALREADY EXISTS
async def add_job_to_db(description, result):
    # If the result is True and contains majors
    if result[0] and result[1]:
        async with aiosqlite.connect(db_name) as conn:
            # Insert the job into the database
            async with conn.execute("BEGIN") as cursor:
                serialized_list = json.dumps(result[1])  # Convert list to string
                await cursor.execute(
                    '''
                    INSERT INTO jobs (link, major, description) VALUES (?, ?, ?)
                    ''',
                    ("True", serialized_list, description)
                )
                await conn.commit()
                print("Job added to the database")

# Async wrapper for the synchronous GeminiCategorizer function
async def async_gemini_categorizer(description):
    loop = asyncio.get_event_loop()
    try:
        # Run the synchronous function in a thread pool
        result = await loop.run_in_executor(None, GeminiCategorizer, description)
        print(result)
        await add_job_to_db(description, result)
    except google.api_core.exceptions.ResourceExhausted as e:
        print("Quota exceeded, waiting before retrying...")
        await asyncio.sleep(30)  # Wait for 30s before retrying
        result = await loop.run_in_executor(None, GeminiCategorizer, description)
        print(result)
    except google.api_core.exceptions.InternalServerError as error:
        print("INTERNAL SERVER ERROR, WAITING BEFORE RETRYING")
        await asyncio.sleep(30)  # Wait for 30s before retrying
        result = await loop.run_in_executor(None, GeminiCategorizer, description)
        print(result)

# Asynchronous function to process the data with rate limiting
async def process_data(data, rate_limit=5):
    tasks = []
    for i in range(min(20, len(data))):  # Process the first 20 items or the length of data if it's less
        if "description" in data[i]:
            task = asyncio.create_task(async_gemini_categorizer(data[i]["description"]))
            tasks.append(task)
            # Rate limiting: wait for a specified time before making the next request
            if (i + 1) % rate_limit == 0:
                await asyncio.sleep(10)  # Adjust the sleep time as needed
    await asyncio.gather(*tasks)
    

async def main():
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ScrapedContent', 'linkedin-jobs.json')

    with open (json_path, 'r') as file:
        data = json.load(file) # a list of dictionaries containing the job info
    await process_data(data)
    #print(data[19]["description"][:min(20, len(data[0]["description"]))])    
    



# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    

""" for i in range(20):
        if "description" in data[i]:
            print(GeminiCategorizer(data[i]["description"])) """