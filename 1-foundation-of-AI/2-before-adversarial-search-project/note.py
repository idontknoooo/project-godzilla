
# Topics:
# 1. Adversarial Search
# 2. Minimax Algorithm
# 3. Alpha-Beta Pruning
# 4. Evaluation Functions
# 5. Isolation Game Player
# 6. Multi-player, probabilistic Games

# LESSON 8: Introduction to Game Playing
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

# LESSON 9: Advanced Game Playing
# 1. Iterative Deepening DFS (IDS)
# https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf
#   a. Search time is dominated by last level search
#   b. Time: O(b^d) b: branching factor, d: depth
#   c. Space: O(db)
#   d. n = (b^(d+1)-1)/(b-1), n: number of nodes in the tree
# 2. Horizon Effect: Something obvious for human but difficult for computer due to the search is not deep enough
# 3. Evaluating Evaluation Function:
#   a. #my_moves - #opponents_moves
#   b. #my-moves - 2 * #opponents_moves
# 4. Alpha-Beta Pruning
#   a. Alpha: The max lower bound of minimax value
#   b. Beta: The minimum upper bound of the minimax value
#   c. Prune: Omit the process of evaluating, reorder nodes can make more nodes available for pruning
# 5. AI: Clever solutions to Exponential Problems
# 6. 3-Players Max-Max-Max Pruning

# LESSON 11: Search
# 1. Definition of A problem
#   1. Initial State: S_0
#   2. Actions: a_1, a_2 ...
#   3. Result: (s, a) -> s'; take a state & action and return a new state
#   4. GoalTest: (s) -> True | False; take a state and return whether that's the goal
#   5. Path Cost (S_i->S_i+1->S_i+2): Take several states and return the cost of this sequence
#   6. Step Cost (s, a, s'): Take a old state(s), action(a) and new state(s') and return the cost of that step
#   7. Explored: All node we explored except 'frontiers'
#   8. Frontier: The deepest node we can reached next
#   9. Unexplored: Nodes unreached
# 2. Cheapest First Search: A greedy algorithm
#   a. Both Breadth-first search and cheapest-first search can find shortest path, DFS cannot
#   b. BFS and CFS are complete, DFS is not
#   c. Greedy Best-first search will find the goal but may not be the shortest path
#   d. Uniform cost search: Search with minimum cost
# 3. A* Search: Best Estimated Total Path cost first
#   a. Min value of f = g+h = path length + estimated distance
#   b. g(path) = path cost
#   c. h(path) = h(s) = estimated distance to goal
#   d. Goal test works by taking paths off the frontier, not putting paths on the frontier
#   e. Will A* always find the lowest cost path? It depends on the huristic function
# 4. Problem with search
#   a. Domain is fully observable
#   b. The Domain must be know: Must know the set of available actions to us
#   c. Domain must be discrete: Finite number of actions to choose from
#   d. Deterministic: Must know the result of taking an action
#   e. Static: Must be nothing else that can chage the world other than our own action
# 5. "implementation for search.png"
# 6. Pac-man LAB: TODO