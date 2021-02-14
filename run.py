from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import wikipedia
import webbrowser
import datetime

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

"""
 Hello and Welcome to my IRL adaption of the famous Jarvis AI from Marvel. This project is a desktop voice assistant, 
and has multiple functionalities. To run this program, you will need to download a couple of modules, if you dont have
them already. 
"""
webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser
                    ("C:\\Program Files (x86)\\Google\\Chrome\\Application"
                     "\\chrome.exe"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


""" Depending on the time, Jarvis presents himself and greets the user """


def hello():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, I am JARVIS, how may i assist you today ")
    elif 12 <= hour < 18:
        speak("Good Afternoon, I am JARVIS, how may I assist you today")
    else:
        speak("Good night, I am JARVIS how may I assist you today")


""" Created class to input audio from the microphone and understand"""


class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please wait. Adjusting your microphone...")
            R.adjust_for_ambient_noise(source, duration=2)
            speak("Listning...........")
            audio = R.listen(source)
        try:
            print("Trying to Understand..")
            text = R.recognize_google(audio, language='en-US')
            print(">> ", text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    """ Main function with all functionalities currently available"""

    def JARVIS(self):
        hello()
        while True:
            self.query = self.STT()
            if 'exit' in self.query or 'leave' in self.query or 'quit' in self.query or 'shut down' in self.query or 'shutdown' in self.query:
                speak('Goodbye')
                exit(0)

            elif 'open google' in self.query:  # Opens Google
                webbrowser.get('chrome').open('www.google.com')
                speak("opening google")
            elif 'wikipedia' in self.query:  # Searches Wikipedia
                speak('Searching Wikipedia...')
                q = q.replace('wikipedia', '')
                results = wikipedia.summary(q, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)
            elif 'open youtube' in self.query:  # Opens Youtube
                webbrowser.get('chrome').open('youtube.com')
            elif 'play music' in self.query:  # Plays Music (In this case I used a song from a turkish show)
                webbrowser.get('chrome').open('https://www.youtube.com/watch?v=rmIC5fF5Z2c')
            elif 'watch osman' in self.query or 'watch usman' in self.query:  # Plays a turkish show
                webbrowser.get('chrome').open('www.osmanonline.co.uk')
            elif 'best player' in self.query:  # Answers GOAT debate for football(Soccer)
                speak(
                    'Cristiano Ronaldo is the best football player in the world. He has won 5 champions leagues, '
                    '5 ballon dors '
                    'and is not a choker like the second best player, Lionel Messi')
            elif 'the time' in self.query:
                current_time = datetime.now().strftime('%H:%M')
                speak('The time is ' + current_time)
            else:
                speak("I do not have the mental capacity to understand this command.")


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920, 1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
