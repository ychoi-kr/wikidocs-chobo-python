min, max = map(int, input().split())

temp = int(input())

while temp != -999:
    if min <= temp <= max:
        print('Nothing to report')
        temp = int(input())
    else:
        print('Alert!')
        break
    
