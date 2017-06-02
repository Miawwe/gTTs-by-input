from gtts import gTTS
import pyglet, time, os
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

def playVoice():
    voice = pyglet.media.load(f, streaming = False)
    voice.play()

    time.sleep(voice.duration)
    os.remove(f)

for i in range(5):
        speech = input("What should i say: ")

        tts = gTTS(text=speech, lang='en')
        f = "temp.mp3"
        tts.save(f)

        playVoice()
