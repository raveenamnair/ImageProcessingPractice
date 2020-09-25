# For Docs for this visit here:
# https://py-googletrans.readthedocs.io/en/latest/

from googletrans import Translator
import pyttsx3
from LanguageCodes import LANGUAGES

translator = Translator()

# Finding the language. If not found, message is printed
choice = input("What language do you want to translate: ")
found = False
for key in LANGUAGES:
    choice = choice.lower()
    if LANGUAGES.get(key) == choice:
        print("Found! " + choice + " " + LANGUAGES.get(key))
        found = True
        break

if not found:
    print("Language not found")

# Two main things it can do is translate and detect

text = 'എന്റെ പേര്‌ രവീന'
print(translator.detect(text))
# translation is object
translation = translator.translate(text, dest='en')
print(translation)

print(translation.pronunciation)

def getword(word):
    print("in method")
    s = translator.translate(word, dest='ml')
    print(s)
    return s.text


# engine = pyttsx3.init()
# engine.say(translation.pronunciation)
# engine.runAndWait()
