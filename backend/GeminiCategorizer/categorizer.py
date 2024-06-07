#api key AIzaSyCB8dgPhkQNXEAUIELu1z-fAcVH2_9tX5c

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

if api_key is None:
    raise ValueError("API_KEY env variable not set")


genai.configure(api_key=os.environ[API_KEY])
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

#hello