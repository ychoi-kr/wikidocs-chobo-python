import random
import time

import speech_recognition as sr

f = open('japanese_words2.csv', encoding='utf-8')
lines = f.readlines()[::-1]
#random.shuffle(lines)

r = sr.Recognizer()
mic = sr.Microphone()

for line in lines:
    hiragana, kanji, pronunciation = line.split(',')

    correct = None
    retry = False
    while not correct:
        if correct is None:
            print('Read this word!:')
        else:
            print('Let\'s try again:')

        print(hiragana)
        s = input("Press Enter when you ready and then read it(input 's' to skip)")
        if s and s.lower()[0] == 's':
            print("Okay. Let's skip")
            break

        ans = ''
        try:
            with mic as source:
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
    
                print('Recognizing...')
                ans = r.recognize_google(audio, language='ja')
                print(f'You sad "{ans}"')

        except sr.WaitTimeoutError as e:
            print("Sorry. I heard nothing.")
            retry = True
            continue

        except sr.UnknownValueError as e:
            if not retry:
                print('What did you say?')
                retry = True
                continue
            else:
                print("Sorry. Let's skip this.")
                break

        if any([w == ans for w in kanji.split('|')]) or hiragana == ans:
            correct = True
            print('You\'re right!')
        else:
            correct = False
            print(hiragana, 'is pronounced', pronunciation)

    print('-' * 20)
    time.sleep(2)
