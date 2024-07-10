def read(text):
    # 콜론을 기준으로 놀이기구 이름과 제한 조건을 분리합니다.
    ridename, restrictions = text.split(":")
    ridename = ridename.strip()  # 공백 제거
    restrictions = restrictions.strip()

    cmmin = cmmax = None  # 초깃값 설정

    # 제한 조건 분석
    if "~" in restrictions:
        parts = restrictions.split("~")
        cmmin = int(parts[0].strip().replace("cm", "").strip())  # 하한 추출 및 변환
        cmmax = int(parts[1].strip().replace("cm", "").strip())  # 상한 추출 및 변환
    elif "이상" in restrictions and "이하" in restrictions:
        pass  # 문제에 이런 케이스가 없으므로 구현하지 않음
    else:
        if "이상" in restrictions:
            cmmin = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환
        elif "이하" in restrictions:
            cmmax = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환

    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

