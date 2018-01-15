
# Topics:
# 1. Adversarial Search
# 2. Minimax Algorithm
# 3. Alpha-Beta Pruning
# 4. Evaluation Functions
# 5. Isolation Game Player
# 6. Multi-player, probabilistic Games

# 1. Isolation: Unable to move on their turn (in a game)
# 2. Minimax Algorithm: detech bad moves  
#   a. Top of Minimax tree will always be a Max level, since we are trying to build a smart machine, and always start from machine's perspective.
#   b. For each max node, pick max among child nodes
#   c. For each min node, pick min among child nodes
#   d. Minimax algo will need to visit appr. b^d nodes to find optimal move. (b: # of branches, d: depth)
# 3. Mini-Project: TODO
# 4. Max Number of Nodes:
#   log_a(x) = log_b(x)/log_b(a)
#   a. Depth-limited Search: The idea of going as far as we think we can to safely meet our deadline
# 5. Evaluation Function: Predicts which branches will lead to a win, and which ones lead to failure.
# 6. Quiescent Search: Search to a depth for a few nodes (not all) where the recommendation will change much any more. 
#       This is a remedy method to solve "horizon effect", which meaning computing power cannot do fully search for all nodes at the same level.
#       Instead, quiescent search, do deeper search on a few "interested nodes" instead of those quiet ones.