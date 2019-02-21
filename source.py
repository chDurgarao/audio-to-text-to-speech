import speech_recognition as sr
import pyttsx3
e=pyttsx3.init()
r = sr.Recognizer()


a1 =sr.AudioFile('a.wav')
a2 =sr.AudioFile('r.wav')
a3 =sr.AudioFile('u.wav')
a4 =sr.AudioFile('n.wav')

with a1 as source:
    au1 = r.record(source)
with a2 as source:
    au2 = r.record(source)
with a3 as source:
    au3 = r.record(source)
with a4 as source:
    au4 = r.record(source)
    
t1=r.recognize_google(au1)
t2=r.recognize_google(au2)
t4=r.recognize_google(au4)


t3=r.recognize_google(au3)
t33=t3[2]
result=t1+t2+t33+t4
print (result.upper())
e.say(result)
e.runAndWait()
