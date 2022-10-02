from gtts import gTTS
from googletrans import Translator
from playsound import playsound
translator = Translator()
dest = input("Enter the language you want:")
file = open("Sample.txt",encoding = "utf8")
mytext = file.read()
if(dest == "en"):
    language = dest
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("Sample.mp3")
else:
    translated_text = translator.translate(mytext,dest)
    language = dest
    myobj = gTTS(text=translated_text.text, lang=language, slow=False)
    myobj.save("Sample.mp3")
    #playsound('Sample.mp3')

