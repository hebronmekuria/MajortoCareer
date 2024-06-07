#api key AIzaSyCB8dgPhkQNXEAUIELu1z-fAcVH2_9tX5c
API_KEY= "AIzaSyCB8dgPhkQNXEAUIELu1z-fAcVH2_9tX5c"
import google.generativeai as genai
import os


genai.configure(api_key=os.environ[API_KEY])
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

#hello