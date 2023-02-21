import openai
import pyttsx3
 
import os
from dotenv import load_dotenv

from voice import doStuff

# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(command)
    engine.runAndWait()

# Define OpenAI API key 
openai.api_key = os.getenv('API_KEY')

# Set up the model and prompt
model_engine = "text-davinci-003"

prompt = doStuff()


# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
SpeakText(response)