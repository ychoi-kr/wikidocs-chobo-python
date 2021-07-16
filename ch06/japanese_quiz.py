import random
import time

import speech_recognition as sr

f = open('japanese_words.csv', encoding='utf-8')
lines = f.readlines()
random.shuffle(lines)

r = sr.Recognizer()
mic = sr.Microphone()

for line in lines:
    hiragana, kanji, pronunciation = line.split(',')

    correct = None
    while not correct:
        if correct is None:
            print('Read this word!:')
        else:
            print('Let\'s try again:')

        print(hiragana)
        input('Press Enter when you ready and then read it ...')

        with mic as source:
            audio = r.listen(source)

        a = r.recognize_google(audio, language='ja')
        print('Your answer:', a)

        if kanji == a:
            correct = True
            print('You\'re right!')
        else:
            correct = False
            print(hiragana, 'is pronounced', pronunciation)

    print('-' * 20)
    time.sleep(2)
