'''
Chatbot
'''

import pyttsx3
import os

chatbot = pyttsx3.init()

choice = ("""
Operation 1 (Shut Down)
Operation 2 (Notepad)
Operation 3 (Learn)
""")

print(choice)

user = input("Enter number to perform operation: ")
print(user)

if user.strip() == "1":
    chatbot.say("Shutting Down,BYE BYE")
    chatbot.runAndWait()
    os.system("shutdown /s /t 1")

elif user.strip() == "2":
   chatbot.say("Opening notepad")
   chatbot.runAndWait
   os.system("notepad")

elif user.strip() == "3":
    chatbot.say("Lets Learn someting")
    chatbot.runAndWait()
    choice3 = input("Do you want to learn something")
    if choice3.strip() == "yes":
        chatbot.say("Dandadan (ダンダダン), also written as Dan Da Dan, is a Japanese web manga series written and illustrated by Yukinobu Tatsu. It has been serialized in Shueisha's Shōnen Jump+ app and website since April 2021, with its chapters collected in 20 tankōbon volumes as of July 2025. The series follows two teenagers with supernatural powers fighting yōkai and aliens with help from multiple allies. An anime television series adaptation produced by Science Saru aired from October to December 2024. A second season premiered in July 2025.")
        chatbot.runAndWait()

    else:
        chatbot.say("OK bye")
        chatbot.runAndWait()