import os

from asr_handler import AsrHandler
from audio_handler import AudioHandler
from chat_handler import ChatHandler
from tts_handler import TtsHandler
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

audio_handler = AudioHandler(duration=5, fs=44100)
asr_handler = AsrHandler(api_key = api_key)
tts_handler = TtsHandler(api_key = api_key)
gpt = ChatHandler(api_key = api_key)


audio_handler.record_audio()
audio_handler.save_audio('output.wav')

asr_handler.transcribe_file('output.wav')

prompt = asr_handler.get_last_transcription()
answer = gpt.respond(prompt)

tts_handler.generate_response(answer)
#tts_handler.generate_response("Good morning! It is 7AM, time to get you up to speed!")
tts_handler.stream_to_file('openai.mp3')

audio_handler.play_mp3('openai.mp3')
audio_handler.terminate()
