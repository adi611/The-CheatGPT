from IPython.display import Audio
import io
import wave
from gtts import gTTS

def convert_bytes_to_wav(bytes_audio):
    # Load the bytes into an in-memory stream
    stream = io.BytesIO(bytes_audio)

    # Open the stream for reading using wave library
    with wave.open(stream, mode='rb') as wave_file:
        # Extract the audio data and metadata
        sample_width = wave_file.getsampwidth()
        num_channels = wave_file.getnchannels()
        sample_rate = wave_file.getframerate()
        num_frames = wave_file.getnframes()
        audio_data = wave_file.readframes(num_frames)

    # Save the audio data to a wav file
    with wave.open('audio.wav', 'wb') as wav_file:
        wav_file.setparams((num_channels, sample_width,
                            sample_rate, num_frames, "NONE", "Uncompressed"))
        wav_file.writeframes(audio_data)


def text_to_speech(text):
    audio = gTTS(text=text, lang='en', slow=False)
    fp = io.BytesIO()
    audio.write_to_fp(fp)
    return fp
