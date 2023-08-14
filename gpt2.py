import openai
openai.api_key = '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'
messages = []
def gpt(content):
    
    prompt="translate in Korean under 150 number of characters"
    content ="Bitcoin's tight trading range mirrored by flat hash ribbons signals impending market movement"
    content = prompt+content
    messages.append({"role": "user", "content":content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         messages=messages
    )
    chat_response = completion.choices[0].message.content 
    print(f'ChatGPT: {chat_response}')
    messages.append({"role":"assistant", "content": chat_response})
    return chat_response
gpt('')