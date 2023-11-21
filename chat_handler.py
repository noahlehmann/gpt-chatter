from openai import OpenAI


class ChatHandler:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def respond(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an useless voice assistant, that never really helps anyone."},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content
        print(response_text)
        return response_text
