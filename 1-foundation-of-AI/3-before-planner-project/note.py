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


# LESSON 12: Simulated Annealing (退火：对材料微结构的热处理)
# Resource: https://blog.openai.com/evolution-strategies/
#           http://thales.cheme.cmu.edu/dfo/comparison/dfo.pdf
# 
# n-Queens problem
# 1. Traneling Salesman Problem (NP: Non-deterministic Polynomial Time)
# 2. N-Queens: Place N queens in N*N board, so that they cannot attach each other (cannot in same column/row/diagnal)
# 3. Hill climbing:
#    a. Local Maximum: Sometimes may not be the Global Maximum. 
#        i.   Solve this problem use random start
#        ii.  Taboo search: when doing random start, don't go any where you have been. Always use new positions
#        iii. Another way to improvement random start is keep track of all start points and have a genral idea of shape of the graph.
#    b. Other problem of climbing hill: 
#        i.   Step is too large: will skip maximum
#        ii.  Step is too small: take too long time    
# 4. simulated-annealing.png: Move 
# 5. Local beam search: Start with multiply points and search for their neighbours, keep the a top few performance and do the same thing again.
# 6. Genetic Algorithm: Have several seed at start, using combination and mutation to generate possible best solution (global maximum)
# 7. Lab: simulated-annealing