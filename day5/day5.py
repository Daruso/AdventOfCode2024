# part 1
# import math

# f = open('input.txt')

# lines = []

# rulesSection = True

# ruleDict = {}

# runningTotal = 0

# for line in f:
#     if line == '\n':
#         rulesSection = False

#     if rulesSection:
#         rule = line[0:-1].split('|')

#         if int(rule[0]) not in ruleDict.keys():
#             ruleDict[int(rule[0])] = [int(rule[1])]
#         else:
#             ruleDict[int(rule[0])].append(int(rule[1]))

#     else:
#         lines.append(line[0:-1].split(','))

# lines.pop(0)

# for line in lines:
#     length = len(line)
#     valid = True
#     for index in range(0,length):
#         numberToBeChecked = int(line[index]) # loop through the successors to see if they appear after our current number
#         if valid and numberToBeChecked in ruleDict.keys(): # sometimes the number is not a key, we cannot check those
#             for successor in ruleDict[numberToBeChecked]: # loop throught the successors
#                 if str(successor) in line: # can only find the successor if it is in the string

#                     if line.index(str(successor)) < index: # check whether the succesors index is lower than our current
#                         valid = False
#                         print('Invalid')
#                         break
#         # else: break
#     if valid:
#         print(line)
#         middle_index = int(length / 2)
#         runningTotal += int(line[middle_index])

# print(runningTotal)

# part 2

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

lines.pop(0)

reorderedLines = []

def checkLine(line, wasIncorrect):
    # print("Called checkLine with: ", line, "\n", "and wasIncorrect: ", wasIncorrect)
    length = len(line)
    for index in range(0,length):
        numberToBeChecked = int(line[index]) # loop through the successors to see if they appear after our current number
        if numberToBeChecked not in ruleDict.keys(): # sometimes the number is not a key, we cannot check those. Add here for ease of use
            ruleDict[numberToBeChecked] = []

        for successor in ruleDict[numberToBeChecked]: # loop throught the successors
            if str(successor) in line: # can only find the successor if it is in the string
                successorIndex = line.index(str(successor))
                numberToBeCheckedIndex = line.index(str(numberToBeChecked))
                if successorIndex < numberToBeCheckedIndex: # check whether the succesors index is lower than our current
                    wasIncorrect = True # we only want to return lines that were incorrect
                    # print("Going from: ", line)
                    line[line.index(str(successor))] = str(numberToBeChecked)
                    line[index] = str(successor)
                    # print("To: ", line)
                    checkLine(line, wasIncorrect)
    if wasIncorrect: return line

for line in lines:
    reorderedLines.append(checkLine(line, False))

for line in reorderedLines:
        print(line)
        if(line is not None):
            middle_index = int(len(line) / 2)
            runningTotal += int(line[middle_index])

print(runningTotal)