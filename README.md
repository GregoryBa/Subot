# Subot - chatbot
Simple chatbot designed for University of Kent students.

## Introduction
Subot is a chatbot able to tell students when different facilities on campus are open, without having to worry about spelling. (The bot is able to answer questions even if the spelling is incorrect) It includes intents.json file that can be easiely edited to add new conversations and even functinalities. It is intended to be easily trained for user without much coding experience. In order to add your own chat intents, edit intents.json file. (Keep the format the same as other intents!) The model provided is already trained and it is not needed to be trained again (unless new intents/functions) are added. The prebuild intents include opening hours of various facilities around the campus, help option that tell you emergency and campus security number, and some random fun facts.


EDIT: When testing on different machines I've came to conclusion that training it beforehand might be necessery. Therefore the code for loading previous training data is commented. (in Chatbots.py)
WARNING: Because of difficulties uploading the windows versions, the .exe files were removed from both windows versions.

## Technologies
Python 3.7.4

## Libraries
nltk
time
numpy
gtts
tflearn
tensorflow
random
pygame
json
pickle
tkinter
mixer

## Versions:
- Linux version with text-to-speech: full version. Linux full version is the most stable one, without delays unlike windows full version has. This is the most efficient and user-friendly version. (STABLE)

- Windows version with text-to-speech: full version. Recommended to run it through Main.py (which should run flawlessly), instead of Main.exe. There are still some problems with Main.exe, considering pygame library used for text-to-speech. (UNSTABLE)

- Windows version without text-to-speech: since the full version didn't work on some of the machines I've tested it on, this version is recommended when the full version crashes. (STABLE)

- Linux version without text-to-speech: This version is NOT included. (STABLE)

## Launch
Python 3.7 (or higher) need to be installed on the users machine. In order to proceed to second step, make sure pip is installed correctly. (Type pip in commandline) Before launching the program, make sure all the python libraries are installed. In order to do that use: 'pip install <library>', for libraries listed above.
To launch the application, in commandline, find the path of the program and execute the following line
python Main.py build
, or depending on your operating system open it in file explorer.

Windows:
There is a Main.exe file in the main directory that can directy run the program. In case of any error proceed to the method below.
Full version with tts might have problems with pygame library. If that happens try stable version without tts.

If higher answer accuracy is needed change the amount of epochs in Chatbots.py (see comments in the code). This tweak is only needed if a lot of new intents are added.

The program is intentionally written to open console and GUI at the same time. This is just to get all the information of what is happening in the background as well as user interface. If a pure GUI version is needed install pyinstaller, in terminal go to main directory of the program and execute following code: (Tested on Linux only)
pyinstaller --window --onefile Main.py

WARNING! pyinstaller 3.5 has problems with nltk library. In order to avoid bugs, find and open hook-nltk.py and manually input the path to the nltk library located in your machine. pyinstaller 3.3 does not have this issue, if possible it is recommended using this version.

## API's not included in the final version:
Because of some difficulties there are a few functions that are not included. The not included API's are:
	- Weather API
	- Timezone API 
	- Music Player API