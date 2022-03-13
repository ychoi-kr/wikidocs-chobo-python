num = int(input())
result = str(num)
    
if num >= 1000000000000000000:
    result = str(num // 1000000000000000000) + 'E'
elif num >= 1000000000000000:
    result = str(num // 1000000000000000) + 'P'
elif num >= 1000000000000:
    result = str(num // 1000000000000) + 'T'
elif num >= 1000000000:
    result = str(num // 1000000000) + 'G'
elif num >= 1000000:
    result = str(num // 1000000) + 'M'
elif num >= 1000:
    result = str(num // 1000) + 'k'
elif num >= 0:
    pass
    
print(result)
