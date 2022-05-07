import sys

sys.path.append("../ch03")
import ridereader


rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''


def allowedrides(height):
    assert type(height) == int

    result = [] 
    for ride in rides.splitlines():
        ridename, cmmin, cmmax = ridereader.read(ride)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
    
    return result


if __name__ == "__main__":
    height = int(input())
    for x in allowedrides(height):
        print(x)

