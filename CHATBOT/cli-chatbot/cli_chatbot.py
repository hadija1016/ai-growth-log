from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
messages=[]
print ("chatbot ready; lets start talking")
while True:
    user_input= input("You:")
    if user_input.lower()=="quit":
        break
    messages.append({"role":"user","content":user_input})
    response =client.chat.completions.create(
    model= "google/gemma-3-4b-it:free",
    messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Bot: {reply}\n")