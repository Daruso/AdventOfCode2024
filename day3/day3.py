# part 1
# import re

# f = open('input.txt')

# lines = []

# runningTotal = 0

# for line in f:
#     line = line[0:-1]
#     lines.append(line)
#     multiplications = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
#     for mult in multiplications:
#         print(mult)
#         numbers = re.findall('\d{1,3}', mult)
#         runningTotal += int(numbers[0])*int(numbers[1])
    
# print(runningTotal)

# part 2
import re

f = open('input.txt')

lines = []
multiplicationList = []
runningTotal = 0

for line in f:
    line = line[0:-1]
    lines.append(line)
    multiplications = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    
    multiplicationList.append(multiplications)

enabled = True
for multiplications in multiplicationList:
    for mult in multiplications:
        print(mult)

        if mult in ['do()', "don't()"]:
            if mult == "do()":
                enabled = True
            else:
                enabled = False
        
        elif enabled:
            numbers = re.findall('\d{1,3}', mult)
            runningTotal += int(numbers[0])*int(numbers[1])
    
print(runningTotal)