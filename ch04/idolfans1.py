njfans = ['철수', '영희', '민수', '지현', '서연']
ivfans = ['영희', '민수', '지수', '서연', '하나']
asfans = ['철수', '지현', '지수', '서연', '나영']

answer = []
for x in njfans:
    if (x in ivfans) and (x not in asfans):
        answer.append(x)

print(','.join(answer))
