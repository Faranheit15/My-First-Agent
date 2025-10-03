from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code != 200:
        return "Could not fetch weather data."
    return f"The current weather in {city} is: {response.text}"

def main():
    user_query = input("> ")
    reponse = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": user_query}]
    )

    print(f"🤖: {reponse.choices[0].message.content}")
    
if __name__ == "__main__":
    # main()
    print(get_weather("Goa"))