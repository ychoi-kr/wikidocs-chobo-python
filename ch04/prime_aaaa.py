def prime(snum):
    print(f"Prime Number List Of {snum}")
    ls = []
    if int(snum) >=2:
        ls = [2] #2는 기본으로 넣어줌
    for s in range(3,int(snum)+1):
        isPrime = False       
        if s%2 !=0: #2로 나눠지는 짝수는 제외,범위를 반으로 줄임.
            for s2 in range(3, s+1, 2): #3 +2값들만 나누기하면됨.
                isPrime = True
                if s%s2 ==0 and s !=s2:
                    isPrime = False
                    break   #그이전에 나눠지면 소수 아님,바로 빠져나옴.                 
        if isPrime == True:
            ls.append(s)           
    print(f"{ls}")   