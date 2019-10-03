from pygame import mixer
from gtts import gTTS

class ChatbotTTS(object):
    def speak(self, ttstext):
        tts = gTTS(text=ttstext, lang="en-us")
        tts.save("response.mp3")
        # call(["mpg321", "answer.mp3"])
        mixer.init()
        mixer.music.load('response.mp3')
        mixer.music.play()