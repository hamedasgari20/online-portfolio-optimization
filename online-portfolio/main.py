

# import libraries
import pandas as pd
from algorithms import best_performing, worst_performing


# Step 1: Read required dataset
S = pd.read_csv('datasets/test_data_2.csv')


# Step 2: Run each strategy on dataset to obtain weight matrix
W_best_performing = best_performing.highest_performing_strategy(S)
W_worst_performing = worst_performing.worst_performing_strategy(S)


# Step 3: Save weights of each strategy
W_best_performing.to_csv(f'weights/weights of strategy best_performing.csv', index=False)
W_worst_performing.to_csv(f'weights/weights of strategy worst_performing.csv', index=False)


# Step 4: Calculate performance of each strategy (transaction cost & Sortino Ratio)