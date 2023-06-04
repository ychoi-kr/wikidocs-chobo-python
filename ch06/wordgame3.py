with open("korean_words.txt") as f:
    voca = set(f.read().split()) 

init_word = '기차'
print('끝말잇기를 하자. 내가 먼저 말할게.\n' + init_word)
spoken_words = [init_word]


def trans_first(word):
    s1 = "냥녀뇨니라락란래량려렷로론뢰료루류륜리"
    s2 = "양여요이나낙난내양여엿노논뇌요누유윤이"
    tt = str.maketrans(s1, s2)
    return word[0].translate(tt) + word[1:]


while True:
    user_input = input('> ')

    if not user_input:
        continue
    elif user_input == "졌다":
        print('야호!')
        break
    elif (
        user_input[0] != spoken_words[-1][-1]
        and user_input[0] != trans_first(spoken_words[-1][-1])
    ):
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif user_input in spoken_words:
        print('아까 했던 말이야. 내가 이겼어!')
        break
    elif user_input not in voca:
        print('사전에 없는 말이야. 내가 이겼지롱~')
        break
    else:
        spoken_words.append(user_input)
        my_word = None
        for word in list(set(voca) - set(spoken_words)):
            if (
                word[0] == user_input[-1]
                or word[0] == trans_first(user_input[-1])
            ):
                my_word = word
                break
       
        if not my_word:
            print('모르겠다. 내가 졌어.')
            break
        else:
            print(my_word)
            if my_word not in voca:
                print('사전에 없는 말이네. 내가 졌어.ㅠ')
            spoken_words.append(my_word)
            continue
    
