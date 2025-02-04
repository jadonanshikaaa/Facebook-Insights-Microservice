import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(page_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Summarize this page:"},
                  {"role": "user", "content": str(page_data)}]
    )
    return response["choices"][0]["message"]["content"]
