lines = []
with open("day1input.txt", "r") as f:
    for line in f: 
        lines.append(line.strip())

digits = '0123456789'
num_digits = [x for x in digits]
word_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0
for line in lines:
    digits = []
    for index, char in enumerate(line): 
        if char in num_digits: 
            digits.append(int(char))
        else:
            for d in word_digits: 
                isDigit = True
                for i, c in enumerate(line[index:]):
                    if len(line[index:]) < len(d): 
                        isDigit = False
                        break
                    try:
                        if c != d[i]:
                            isDigit = False
                            break
                    except:  
                        break 
                if isDigit:
                    digits.append(word_digits.index(d))
                    break
    sum += int(str(digits[0]) + str(digits[-1]))

print(sum)
