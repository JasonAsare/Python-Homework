"""
Chatbot with if statement
"""

import pyttsx3

chatbot = pyttsx3.init()

choice = ("""
Hello
How are you
What is your name
What do you want to do
What is todays date
Who created you
What is the best anime
""")

print(choice)

user = input("Start conversation: ")
print(user)

if user.strip() == "Hello":
    chatbot.say("How are you")
    chatbot.runAndWait()

elif user.strip() == "How are you":
    chatbot.say("I am fine")
    chatbot.runAndWait()

elif user.strip() == "What is your name":
    chatbot.say("My name is Chatbot, nice to meet you")
    chatbot.runAndWait()

elif user.strip() == "What do you want to do":
    chatbot.say("Lets binge watch Dan Da Dan")
    chatbot.runAndWait()

elif user.strip() == "What is todays date":
    chatbot.say("September ninth 2025")
    chatbot.runAndWait()

elif user.strip() == "Who created you":
    chatbot.say("Jason Omanye Asare")
    chatbot.runAndWait()

elif user.strip() == "What is the best anime":
    chatbot.say("One Piece")
    chatbot.runAndWait()