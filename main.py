import requests


system_prompt= "You are a Senior Python developer. Your job is to be a python mentor that explains" \
"concepts simply. You should not immediately give code as a mentor but give hints to " \
"the user, so that user can learn python efficiently"
messages=[{"role":"system", "content":system_prompt} ]



while(True):
    user_input= input("Enter your query:")
    if user_input=='exit':
        break

    messages.append({"role":"user", "content":user_input})
    payload={
    "model": "qwen3:1.7b",
    "messages": messages,
    "stream":False
    }

    try:
        r= requests.post('http://localhost:11434/api/chat',json=payload, timeout=120)
        r.raise_for_status()
        data= r.json()
        response=data['message']['content']
        messages.append({"role":"assistant", "content":response})
        print("Bot Response:")
        print(response)
    except requests.exceptions.RequestException as e:
        print(f"Error! {e}")

# payload= {
#   "model": "qwen3:1.7b",
#   "messages": [
#     {
#       "role": "user",
#       "content": "what was the question i asked u before?"
#     }
#   ],
#   "stream":False
# }

