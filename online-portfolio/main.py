from tools import rate_of_return, transaction_cost, portfolio_return, sortino_ratio
import pandas as pd
from algorithms import nsga2


# Step 1: Select required dataset from directory datasets
S = pd.read_csv('datasets/test_data_1.csv')


# Step 2: Select strategy to obtain weight matrix
W = nsga2.strategy(S)


# Step 3: Save weights of each strategy
W.to_csv(f'weights/weights of strategy.csv', index=False)


# Step 4: Calculate performance of each strategy (transaction cost & sortino ratio & rate of return)
R = rate_of_return(S)
# R.to_csv(f'R.csv', index=False)
TC = transaction_cost(W, alfa=0.005)
ROR = portfolio_return(W, R)
SORTINO_RATIO = sortino_ratio(W, R, risk_free_rate=0)


print(f'transaction cost (%) initial deposit: ' + str(round(TC, 3)))
print(f'sortino ratio is: ' + str(round(SORTINO_RATIO, 3)))
print(f'rate of return portfolio (%) initial deposit: ' + str(round(ROR, 3)))
