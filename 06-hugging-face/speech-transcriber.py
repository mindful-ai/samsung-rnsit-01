import requests
import soundfile
from transformers import pipeline
import io

MODEL = "openai/whisper-large-v3"
AUDIO = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"

transcriber = pipeline(
        task="automatic-speech-recognition",
        model=MODEL
)

audio_bytes = requests.get(AUDIO).content
audio, samplerate = soundfile.read(io.BytesIO(audio_bytes))


result = transcriber(audio)
print(result)