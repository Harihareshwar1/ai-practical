import math

max_player = 1
min_player = -1

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
  if depth == 3:
    return values[nodeIndex]

  if maximizingPlayer:
    best = -math.inf

    for i in range(0, 2):
      val = alpha_beta(depth + 1, nodeIndex*2 + i, False, values, alpha, beta)
      best = max(best, val)
      alpha = max(alpha, best)

      if beta <= alpha:
        break
    return best

  else:
    best = math.inf

    for i in range(0, 2):
      val = alpha_beta(depth + 1, nodeIndex*2 + i, True, values, alpha, beta)
      best = min(best, val)
      beta = min(beta, best)

      if beta <= alpha:
        break
    return best

values = [3, 5, 6, 9, 1, 2, 0, -1]


alpha = -math.inf
beta = math.inf

result = alpha_beta(0, 0, True, values, alpha, beta)
print(f'Optimal Value: {result}')