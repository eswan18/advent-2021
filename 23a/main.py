from amphipod import Amphipod

with open('test_input.txt', 'rt') as f:
    lines = f.readlines()

amphis = []
ROOM1 = 3
ROOM2 = 5
ROOM3 = 7
ROOM4 = 9

for line_num in (2, 3):
    for room in [ROOM1, ROOM2, ROOM3, ROOM4]:
        if room == ROOM1:
            if line_num == 2:
                loc = 'l'
            else:
                loc = 'p'
        elif room == ROOM2:
            if line_num == 2:
                loc = 'm'
            else:
                loc = 'q'
        elif room == ROOM3:
            if line_num == 2:
                loc = 'n'
            else:
                loc = 'r'
        elif room == ROOM4:
            if line_num == 2:
                loc = 'o'
            else:
                loc = 's'
        color=lines[line_num][room]
        amphis.append((color, loc))
print(amphis)
