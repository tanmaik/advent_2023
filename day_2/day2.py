colors = ['red', 'green', 'blue']

with open('day2input.txt', 'r') as f: 
    lines = { index + 1 : line.strip().split(": ")[1] for index,  line in enumerate(f)}

# part 1

possibles = []
for index, line in enumerate(lines.values()):
    sets = line.split("; ")
    possible = True

    for set in sets: 
        ball_amount = set.split(", ")
        for ball in ball_amount:
            if ball[-1] == "d":
                try:
                    if int(ball[0:2]) > 12:
                        possible = False
                except: 
                    pass
            elif ball[-1] == "e":
                try:
                    if int(ball[0:2]) > 14:
                        possible = False
                except: 
                    pass
            elif ball[-1] == "n":
                try:
                    if int(ball[0:2]) > 13:
                        possible = False
                except: 
                    pass


    if possible: 
        possibles.append(index + 1)

print(sum(possibles))

# part 2

sum = 0
for index, line in enumerate(lines.values()):
    reds = []
    greens = []
    blues = []

    sets = line.split("; ")

    for set in sets: 
        ball_amount = set.split(", ")
        for ball in ball_amount:
            if ball[-1] == "d":
                try:
                    reds.append(int(ball[0:2]))
                except: 
                    reds.append(int(ball[0]))
            elif ball[-1] == "e":
                try:
                    blues.append(int(ball[0:2]))
                except: 
                    blues.append(int(ball[0]))
            elif ball[-1] == "n":
                try:
                    greens.append(int(ball[0:2]))
                except: 
                    greens.append(int(ball[0]))
    sum += (max(reds) * max(greens) * max(blues))
print(sum)