symbols = '!@#$%^&*()_+{}|:"<>?`-=[]\;\',./'
schematic = []
with open('day3input.txt', 'r') as f: 
    for line in f: 
        schematic.append([char for char in line.strip()])

print(schematic)
