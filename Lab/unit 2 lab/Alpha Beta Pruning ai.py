def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 0:
        return values[node]

    if maximizing:
        best = -1000

        for i in range(2):
            val = alphabeta(depth-1, node*2+i,
                            alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth-1, node*2+i,
                            alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(3, 0, -1000, 1000, True)

print("Best Value:", result)
