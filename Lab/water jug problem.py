from collections import deque

start = (0, 0)
goal = 2
q = deque([start])
visited = {start}

while q:
    a, b = q.popleft()
    print(a, b)

    if a == goal or b == goal:
        print("Target reached")
        break

    pour = min(a, 3 - b)

    states = [
        (4, b),
        (a, 3),
        (0, b),
        (a, 0),
        (a - pour, b + pour),
        (min(a + b, 4), max(0, a + b - 4)),
        (min(3, a + b), 0)
    ]

    for s in states:
        if s not in visited:
            visited.add(s)
            q.append(s)
