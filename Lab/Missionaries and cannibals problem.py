from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state == goal:
        for s in path:
            print(s)
        break

    for x, y in moves:
        if boat == 1:
            nm, nc, nb = m - x, c - y, 0
        else:
            nm, nc, nb = m + x, c + y, 1

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if ((nm == 0 or nm >= nc) and
                (3-nm == 0 or 3-nm >= 3-nc)):
                new = (nm, nc, nb)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [new]))
