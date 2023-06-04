my_voca = """
기차
차량
양심
차박
박쥐
쥐구멍
멍게
게맛살
살구
구멍
멍청이
이빨
빨대
대롱
롱다리
리본
본네트
트라이앵글
글라이더
더치페이
이자
자율
""".split()

init_word = '기차'
print('끝말잇기를 하자. 내가 먼저 말할게.\n' + init_word)
spoken_words = [init_word]


def trans_first(word):
    s1 = "라락란량로료리"
    s2 = "나낙난양노뇨이"
    tt = str.maketrans(s1, s2)
    return word[0].translate(tt) + word[1:]


while True:
    user_input = input('> ')
    
    if not user_input:
        continue
    elif user_input == "졌다":
        print('야호!')
        break
    elif user_input[0] != spoken_words[-1][-1]:
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif user_input in spoken_words:
        print('아까 했던 말이야. 내가 이겼어!')
        break
    else:
        spoken_words.append(user_input)
        my_word = None
        for word in list(set(my_voca) - set(spoken_words)):
            if word.startswith(trans_first(user_input[-1])):
                my_word = word
                break
       
        if not my_word:
            print('모르겠다. 내가 졌어.')
            break
        else:
            print(my_word)
            spoken_words.append(my_word)
            continue
    
