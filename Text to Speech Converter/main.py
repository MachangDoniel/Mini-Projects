from gtts import gTTS
import os

f = open('text.txt')
x = f.read()

language = 'en-us'  # Use 'en-us' for a male voice

audio = gTTS(text=x, lang=language, slow=False)

audio.save("text.wav")
os.system("text.wav")
print("Text to Voice conversion successfull.")