import openai 




def ask_gpt(key, user_prompt , user_temp = 0.5 , user_max_tokens = 500 ):
    openai.api_key = key

    completion = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=user_prompt,
    max_tokens=user_max_tokens,
    temperature=user_temp
    )

    return completion.text[0]
