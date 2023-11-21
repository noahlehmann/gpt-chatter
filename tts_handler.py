from openai import OpenAI


class TtsHandler:

    def __init__(self, api_key, model='tts-1'):
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.responses = []

    def generate_response(self, text_input):
        response = self.client.audio.speech.create(
            model=self.model,
            voice="alloy",
            input=text_input
        )
        self.responses.append(response)

    def stream_to_file(self, file_path):
        self.responses[-1].stream_to_file(file_path)
