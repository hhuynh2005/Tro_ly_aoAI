import speech_recognition
import pyttsx3
#mieng robot
from datetime import date , datetime
robot_ear = speech_recognition.Recognizer()

robot_mouth = pyttsx3.init()

robot_brain = ""

while True:
     #lap
    #noi
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("you:" + you)
    #hieu
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif you =="hello":
        robot_brain = "hello hoang huynh"

    elif you == "today": 
    #phai co dau : 
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")

    #biet ngay: get current datem python
    elif you == "ngay":
        now = datetime.now()
        robot_brain = now.strptime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "bye hoang huynh"
        print("Robot:" + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
        
    else: 
        robot_brain = "I'm fine thank you and you"
    #noi

    print("Robot:" + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()