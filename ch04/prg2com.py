import copy

def sol1(inlist, coms):
    _inlist = copy.deepcopy(inlist)
    outlist = []
    sumout = []

    for i in range(coms):
        outlist.append([])
        sumout.append(0)
    
    # 프로그램들을 전부 수행하는 데 걸리는 총수행시간을 구한다.
    total_time = sum(_inlist)
    
    #총수행시간을 컴퓨터 대수로 나누어 각각의 컴퓨터의 평균수행시간을 구한다.
    avg_time = total_time / coms
    
    for j in range(coms):

        # 평균수행시간보다 오래 걸리는 프로그램이 있으면 그냥 컴퓨터에게 준다.
        if True in [k >= avg_time for k in _inlist]:
            for m in _inlist:
                if m >= avg_time:                    
                    outlist[j].append(m)
                    _inlist.remove(m)
                    sumout[j] += m
                    break

        # 평균 수행시간보다 짧게 걸리는 것들은 모아서 컴퓨터에게 준다.
        else:
            for n in range(len(_inlist)):
                if _inlist[n] == 0:
                    continue
                v = _inlist[n]
                outlist[j].append(v)
                _inlist[n] = 0
                sumout[j] += v
                if sumout[j] >= avg_time:
                    break
    
    return outlist


def sol2(inlist, coms):
    _inlist = copy.deepcopy(inlist)
    outlist = []
    sumout = []
    for x in range(coms):
        outlist.append([])
        sumout.append(0)
    
    _inlist.sort(reverse=True)

    # 수행할 작업을 빵(bread)에, 컴퓨터를 바구니(basket)에 비유
    for bread in _inlist:
        lowbasket = sumout.index(min(sumout)) # 가장 가벼운 바구니에
        outlist[lowbasket].append(bread) # 빵을 담는다
        sumout[lowbasket] += bread

    return outlist

if __name__ == '__main__':
    
    inlist = [3,5,2]
    coms = 2
    optimal = [[5], [3, 2]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')
    
    inlist = [3,15,6,22,13,2]
    coms = 3
    optimal = [[22], [15, 6], [13, 3, 2]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')

    inlist = [7,8,9,10,11]
    coms = 2
    optimal = [[11, 10], [9, 8, 7]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))

