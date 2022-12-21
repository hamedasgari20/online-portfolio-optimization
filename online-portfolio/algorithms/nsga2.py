from utils import *


s = pd.read_csv('../datasets/test_data_1.csv')

def strategy(s):
    w = s * 0
    for i in range(1, len(s)):
        # for each row in matrix s find nsga2 result and save it in w
        w.iloc[i] = nsga2(s, w, i, population=3, max_gen=1)
    return w
result = strategy(s)
print(result)