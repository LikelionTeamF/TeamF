import openai
#openai.api_key = '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'
openai.api_key = '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'
messages = []
def gpt_title(content):
    messages = []
    prompt="다음 내용을 한국어로 번역해 줘. 번역한 내용만 출력해줘. 대답하지 말고."
    #content ="Bitcoin's tight trading range mirrored by flat hash ribbons signals impending market movement"
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


def gpt_content(content):
    messages = []
    prompt="Translate following document in Korean"
    #content ="Bitcoin's tight trading range mirrored by flat hash ribbons signals impending market movement"
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