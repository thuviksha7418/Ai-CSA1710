colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = {}

def coloring(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for color in colors:
        if all(result.get(n) != color for n in graph[region]):
            result[region] = color

            if coloring(node + 1):
                return True

            del result[region]

    return False

if coloring(0):
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution found")
