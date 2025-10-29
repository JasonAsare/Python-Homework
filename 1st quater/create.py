import pyttsx3
house_ai = pyttsx3.init()

PASSWORD = "2qn3"

house_ai.say("Hello i am house ai how can i help you")
house_ai.runAndWait()

list = ("""
Open door
Ask question
Security mode
""")

print(list)
user = input("Enter what you want to do: ")

if user == ("Open door"):
    house_ai.say("Enter password: ")
    house_ai.runAndWait()
    p = input("Password: ")
    if p == (PASSWORD):
        house_ai.say("Doors opening")
        house_ai.runAndWait()
    else:
        house_ai.say("Incorrect password, go away thief")
        house_ai.runAndWait()

if user == ("Ask question"):
    house_ai.say("What do you want to know")
    house_ai.runAndWait()
    q = input("Question: ")
    question_list = ("""
    What is the password
    What is your name
    Who owns this house
    Can i buy you
    """)
    if q == ("What is the password"):
        house_ai.say("Why are you a thief")
        house_ai.runAndWait()
    if q == ("What is your name"):
        house_ai.say("My name s house_ai")
        house_ai.runAndWait()
    if q == ("Who owns this house"):
        house_ai.say("Jason Asare")
        house_ai.runAndWait()
    if q == ("Can i buy you"):
        house_ai.say("No")
        house_ai.runAndWait()
if user == ("Security mode"):
    house_ai.say("Entering securiy mode")
    house_ai.runAndWait()