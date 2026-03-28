from openai import OpenAI
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
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