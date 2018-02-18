# LESSON 17: Bayes Nets
# 1. Bayes Network: 
#   1. Need 2 variables (A & B). 
#   2. Know P(A) & P(B|A) & P(B|!A)
#   3. Want to know P(A|B) & P(A|!B)
#   4. All above is called entire network of Bayes net
# 2. Bayes Rule
#   P(A|B) = P(B|A)P(A) / P(B)
#   P(!A|B) = P(B|!A)P(!A) / P(B)
#   P(A|B) + P(!A|B) = 1
# 3. Other Probability Rules:
#   P(AB) = P(A|B)P(B) = P(B|A)P(A) 
# 4. Conditional Independence
#   P(AB|T) = P(A|T)*P(B|T) 
#   Conditional Indenpendence != Absolute Independence, they don't imply each other either
# 5. Different Type Of Bayes Network
# 6. D Separation 

# LESSON 18: Inference Of Bayes Nets
# 1. Evidence Node: Variables that we know the values of. 
# 2. Query Node: Variables that we want to find out the values of. 
# 3. Hidden Node: Anything that is neither evidence nor query node. 
# 4. Enumeration: Read Probability Table
# 5. Causal Direction: Inference flow from causes to result. 
# 6. 