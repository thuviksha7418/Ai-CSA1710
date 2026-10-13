from heapq import *

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

def solve(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        i = state.index(0)

        for j in [i-3, i+3, i-1, i+1]:
            if 0 <= j < 9 and abs(i//3-j//3) + abs(i%3-j%3) == 1:
                new = list(state)
                new[i], new[j] = new[j], new[i]
                new = tuple(new)

                if new not in visited:
                    heappush(pq, (g+1+heuristic(new),
                                  g+1, new, path+[state]))

    return None

result = solve(start)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
