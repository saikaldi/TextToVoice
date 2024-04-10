import pyttsx3 as p

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
print(rate)
engine.say("I will speak this text")
engine.runAndWait()
