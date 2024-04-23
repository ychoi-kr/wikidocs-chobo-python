def read(text):
    ridename, limit = map(str.strip, text.split(':'))
    
    cmmin = cmmax = None
    if '~' in limit:
        cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif "이상" in limit:
        cmmin = int(limit.split("cm")[0])

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

