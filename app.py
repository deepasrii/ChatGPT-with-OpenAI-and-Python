import openai

openai.api_key = "OPENAI_SECRET_KEY"

while True:
    
    prompt = input("Ask Anything to OpenAI Chatbot: ")
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.9,
                                        max_tokens=500,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0.6
                                        )
    
    text = response['choices'][0]['text']
    print('Reply: '+text)
