##################################################################
##################################################################
##################################################################
# AI INTRODUCTION

# Navigation is an AI problem, which can be better modified by AI
# Heuristic: Some additional piece of information - a rule, a function or constraint that informs an otherwise brute-force algorithm to act in a more optimal manner.
#  启发式算法: 当传统方法速度较慢时，用牺牲准确性，完整性，优化性的方法来实现速度上的提升。
# e.g. Monty Hall Problem (3扇门，其中一个后面有车，另外两个后面有羊)
#   其中，Probability就是一个 Heuristic Function

# Agent: Intelligent system (software)
# Environment: Hardware of agent, all other external object
# State: The behavior of an agent
# Goal State: The objective state
# Perception: Help an agent receive information from environment
# Action: The process of changing a state
# Cognition: The process of an agent decides what action to take based on perception

# Type of AI problems:
#   Fully observable: Ai knows everything
#   Partially observable: Ai only know part of the game
#   Deterministic: Action is predictable
#   Stochastic: Action is random
#   Discrete: Action is limited
#   Continous: Action is unlimited
#   Benign: Ai is the only player
#   Adversarial: Ai has opponents

# What is Intelligence
#   Rational Behavior: An intelligent agent is one that takes action to maximize its expected utility given a desired goal.
#   Bounded Optimality: A way to quantify intelligence. 不是绝对的最优，而是条件下的最优解。


##################################################################
##################################################################
##################################################################
# APPLYING AI TO SUDOKU

# How to solve Sudoku: http://norvig.com/sudoku.html
# 1. Two techniques:
#   Constraint Propagation: Narrow the possibility
#   Search: Handle cases when there is multiply possible solution
# 2. Terms:
#   a. Box: Each indivisual cell
#   b. Unit: Each 3*3 square
#   c. Peer: A particular box which belong to a common unit or in same row/column of current box
# 3. Encoding The board
#   a. rows = 'ABCDEFGHI'
#   b. cols = '123456789'
#   c. Matrix
#       {
#       'A1': '.'
#       'A2': '.',
#       'A3': '3',
#       'A4': '.',
#       'A5': '2',
#       ...
#       'I9': '.'
#       }
# 4. Strategy 1: Elimination
#   For each box, assign number to all other boxes and eliminate possibilities
# 5. Strategy 2: Only Choice
#   No other cell available for this number
# 6. Strategy 3: Search
#   Depth First Search


##################################################################
##################################################################
##################################################################
# ANACONDA
# 1. Create Anaconda environment:
#   conda create -n tea_facts python=3
# 2. Enter environment
#   source activate tea_facts
# 3. Check condalist
#   conda list
# 4. Install packages
#   conda install numpy pandas matplotlib
# 5. Install Jupyter Notebook
#   conda install jupyter notebook
# 6. Create environment
#   conda create -n my_env python=3 numpy 
#   conda create -n py2 python=2
# 7. Stop Environment
#   source deactivate
# 8. Export Environment Setting
#   conda env export > environment.yaml
#   conda env export > environment.yml
# 9. Create Environment from file
#   conda evn create -f environment.yaml
# 10. List Environments
#   conda env list
# 11. Remove Environments
#   conda env remove -n env_name
# 12. Sharing Environments
#   pip freeze > env.txt