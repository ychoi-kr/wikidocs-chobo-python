colwidth = 61
rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}

half = colwidth // 2
line = '0' * half + '1' + '0' * half
print(line)

while line[1] == '0':
    prev = line
    line = '0' * colwidth
    for i in range(1, colwidth - 1):
        line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
    print(line)
    
