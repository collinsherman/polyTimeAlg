# STRING is the input string; i, l and n will never change.
STRING = 'baba'

# '&' denotes the empty set
ruleList = ['SRT', 'RTR', 'Ra', 'TTR', 'Tb']
gridTable = {}

n = len(STRING) + 1
empty = '&'
positionList = []


for x in range(1, n):
    for y in range(1, n):
        positionList.append('(' + str(x) + ', ' + str(y) + ')')

for pos in positionList:
    gridTable[pos] = ''

if any(empty in x for x in ruleList) == True:
    if 'S&' in ruleList:
        print("Accept")
    else:
        print("Reject")

else:
    for x in range(1, n):    
        for char in STRING[x - 1:x]:
            for rule in ruleList:
                if char in rule:
                    gridTable['(' + str(x) + ', ' + str(x) + ')'] = rule[:1]
            
    for x in range(2, n):
        for y in range(1, n - x + 1):
            j = y + x - 1
            for z in range(y, j):
                for rule in ruleList:
                    k = z + 1
                    aPos = '(' + str(y) + ', ' + str(j) + ')'
                    bPos = '(' + str(y) + ', ' + str(z) + ')'
                    cPos = '(' + str(k) + ', ' + str(j) + ')'
                    if rule[1:2] in gridTable[bPos] and rule[2:] in gridTable[cPos]:
                        if gridTable[aPos] == '':
                            gridTable[aPos] = rule[:1]
                        else:
                            value = gridTable[aPos] 
                            gridTable[aPos] = str(value + ', ' + rule[:1])
    print('+-------' * 4 + '+')
    print('|', sep=' ', end='', flush=True)     
    count = 0              
    for pos in gridTable:
        if gridTable[pos] == '':
            print('       |', sep='', end='', flush=True)
        elif len(gridTable[pos]) == 4:
            print('  ' + gridTable[pos] + ' |', sep='', end='', flush=True)
        elif len(gridTable[pos]) == 7:
            print(gridTable[pos] + '|', sep='', end='', flush=True)
        else:
            print('   ' + gridTable[pos] + '   |', sep='', end='', flush=True)
        count += 1
        if count % 4 == 0 and count < 16:
            print('')
            print('+-------' * 4 + '+')
            print('|', sep='', end='', flush=True)
    print('')    
    print('+-------' * 4 + '+')

    if 'S' in gridTable['(1, ' + str(n - 1) + ')']:
        print('Accept')
    else:
        print('Reject')
