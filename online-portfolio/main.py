# todo check sonarlint suggestions
# import libraries
from tools import *
import pandas as pd
from algorithms import best_performing, worst_performing

# Step 1: Read required dataset
S = pd.read_csv('datasets/test_data_2.csv')
R = rate_of_return(S)



# Step 2: Run each strategy on dataset to obtain weight matrix
W = best_performing.highest_performing_strategy(S)
# W = worst_performing.worst_performing_strategy(S)


# Step 3: Save weights of each strategy
W.to_csv(f'weights/weights of strategy best_performing.csv', index=False)
# print(W)



# Step 4: Calculate performance of each strategy (transaction cost & Sortino Ratio)
TC = transaction_cost(W)
ROR = portfolio_return(W, R)
SORTINO_RATIO = sortino_ratio(W, R)

print(f'sortino ratio is: '+ str(SORTINO_RATIO))
print(f'transaction cost is: '+ str(TC))
# todo double check each calculations

