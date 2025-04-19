
#Creating OpenAI key
from openai import OpenAI
from dotenv import load_dotenv #pip install python-dotenv
import os

# Load environment variables from .env file
load_dotenv()

#****Basic Example
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

#****provide image inputs
response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "What country do you think this is?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://images.pexels.com/photos/58597/pexels-photo-58597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                }
            ]
        }
    ]
)
print(response.output_text)
"""
{'error': {'message': "You uploaded an unsupported image. Please make sure your image has of one the following formats: ['png', 'jpeg', 'gif', 'webp'].", 
'type': 'invalid_request_error', 'param': None, 'code': 'invalid_image_format'}}
However when I put: "https://images.pexels.com/photos/58597/pexels-photo-58597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" as url it still accepts
"""
