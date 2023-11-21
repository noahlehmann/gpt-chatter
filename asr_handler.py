from openai import OpenAI


class AsrHandler:

    def __init__(self, api_key, model="whisper-1"):
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.transcriptions = []

    def transcribe_file(self, file_path):
        audio_file = open(file_path, "rb")
        transcript = self.client.audio.transcriptions.create(
            model=self.model,
            file=audio_file
        )
        print(transcript)
        self.transcriptions.append(transcript)

    def get_last_transcription(self):
        return self.transcriptions[-1].text
