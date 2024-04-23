# 개발 알려주는 봇 GPT가 제안한 코드입니다.
# 대화 기록: https://chat.openai.com/share/88c44988-2237-4ec2-ae3f-3d1dbb1d6e6b

def read(text):
    # 콜론을 기준으로 놀이기구 이름과 제한 조건을 분리합니다.
    ridename, restrictions = text.split(":")
    ridename = ridename.strip()  # 공백 제거
    restrictions = restrictions.strip()

    cmmin = cmmax = None  # 초깃값 설정

    # 제한 조건 분석
    if "이상" in restrictions:
        cmmin = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환
    elif "이하" in restrictions:
        cmmax = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환
    elif "~" in restrictions:
        parts = restrictions.split("~")
        cmmin = int(parts[0].strip().replace("cm", "").strip())  # 하한 추출 및 변환
        cmmax = int(parts[1].strip().replace("cm", "").strip())  # 상한 추출 및 변환

    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

