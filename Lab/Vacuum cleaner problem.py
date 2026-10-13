room = {'A': 1, 'B': 1}
position = 'A'

while 1 in room.values():
    if room[position] == 1:
        print("Suck", position)
        room[position] = 0
    else:
        position = 'B' if position == 'A' else 'A'
        print("Move to", position)

print("Both rooms are clean!")
