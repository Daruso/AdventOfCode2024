# part 1 & 2

f = open('input.txt')

runningTotal = 0

def checkLevelRemoval (lineReports):
    length = len(lineReports)
    
    safe = True
    vector = 0

    for index in range(0, length-1):
        difference = int(lineReports[index+1]) - int(lineReports[index])

        if difference > 0 and vector == 0: vector = 1
        if difference < 0 and vector == 0: vector = -1
        if (difference > 0 and vector == -1) or (difference < 0 and vector == 1) or difference == 0: 
            safe = False
            break

        if abs(difference) > 3:
            safe = False
            break

    return safe


for report in f:
    line = report[0:-1]
    lineReports = line.split(' ')
    length = len(lineReports)
    
    safe = True
    vector = 0

    for index in range(0, length-1):
        difference = int(lineReports[index+1]) - int(lineReports[index])

        if difference > 0 and vector == 0: vector = 1
        if difference < 0 and vector == 0: vector = -1
        if (difference > 0 and vector == -1) or (difference < 0 and vector == 1) or difference == 0: 
            safe = False
            break

        if abs(difference) > 3:
            safe = False
            break

    # comment for part 1
    if not safe:
        safe = False
        for index in range (0, length):
            otherReports = lineReports[:index] + lineReports[index+1:]
            if checkLevelRemoval(otherReports):
                safe = True
                break

    if safe: runningTotal+=1

print(runningTotal)