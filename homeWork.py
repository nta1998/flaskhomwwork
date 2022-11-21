import pyttsx3

engine = pyttsx3.init() 

rate = engine.getProperty('rate')  
print (rate)                     
engine.setProperty('rate', 170)     

volume = engine.getProperty('volume')   
print (volume)                          
engine.setProperty('volume',1.0)  

voices = engine.getProperty('voice')     
engine.setProperty('voice', voices[0])  

engine.say("Hello python class")
engine.say('i am jarvis')
engine.say('i am here to help you stady')
engine.say('press 1 to lern about python')
engine.say('or press 2 to lern about flask')

engine.runAndWait()
answer =input()
if answer == "1":
    engine.say('Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling (from the start plus new capabilities in Python 3.11) and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Pythons "benevolent dictator for life a title the Python community bestowed upon him to reflect his long-term commitment as the projects chief decision-maker. In January 2019, active Python core developers elected a five-member Steering Council to lead the project.')
elif answer == "2":
    engine.say('Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries Welcome to Flasks documentation. Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API section.')
engine.runAndWait()

engine.runAndWait()