from gtts import gTTS
from pygame import mixer

speech = input("What should i say: ")

tts = gTTS(text=speech, lang='en')
tts.save("message.mp3")

mixer.init()
mixer.music.load("message.mp3")
mixer.music.play()

while mixer.music.get_busy() == True:
    continue
