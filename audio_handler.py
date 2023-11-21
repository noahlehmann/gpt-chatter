import pyaudio
import wave
import pygame


class AudioHandler:
    def __init__(self, duration=3, fs=44100):
        self.duration = duration
        self.fs = fs
        self.p = pyaudio.PyAudio()

    def record_audio(self):
        stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.fs, input=True, frames_per_buffer=1024)
        print("Recording...")
        frames = []

        for i in range(0, int(self.fs / 1024 * self.duration)):
            data = stream.read(1024)
            frames.append(data)
        print("Recording finished.")

        stream.stop_stream()
        stream.close()

        self.frames = frames

    def save_audio(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print("File saved.")

    def play_wav(self, filename):
        wf = wave.open(filename, 'rb')
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                             rate=wf.getframerate(), output=True)

        print("Playing the audio file...")
        data = wf.readframes(1024)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()

        print("Playback finished.")

    def play_mp3(self, filename):
        # Initialize the mixer
        pygame.mixer.init()

        # Load the mp3
        pygame.mixer.music.load(filename)

        # Play the mp3
        print("Playing the audio file...")
        pygame.mixer.music.play()

        # Wait for the music to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Playback finished.")

    def terminate(self):
        self.p.terminate()
