# part 1

f = open('input.txt')

lines = []

rulesSection = True

ruleDict = {}

runningTotal = 0

for line in f:
    if line == '\n':
        rulesSection = False

    if rulesSection:
        rule = line[0:-1].split('|')

        if int(rule[0]) not in ruleDict.keys():
            ruleDict[int(rule[0])] = [int(rule[1])]
        else:
            ruleDict[int(rule[0])].append(int(rule[1]))

    else:
        lines.append(line[0:-1].split(','))
        # print(line[0:-1].split(','))

lines.pop(0)

for line in lines:
    length = len(line)
    print(line)
    valid = True
    for index in range(0,length):
        if valid:
            for successor in ruleDict[int(line[index])]:
                if successor in 
                    if line.index(str(successor)) < index:
                        valid = False
                        print('Invalid')
                        break
    if valid: runningTotal += 1


print(runningTotal)