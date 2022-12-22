import time
from utils import *


s = pd.read_csv('../datasets/test_data_1.csv')
r = (s / s.shift(1)) - 1
w = s * 0

def strategy(s):

    for i in range(1, len(s)):
        # for each row in matrix s find nsga2 result and save it in w
        obj1, obj2, solution = nsga2(s, w.iloc[i-1, :], r.iloc[i, :], i, population=3, max_gen=1)
        # # In each step pareto layer can seen we two lines below
        # non_dominating_curve_plotter(obj1, obj2)
        # time.sleep(5)
        # TODO find similar w with previous w between best solution found solution[0] is not correct
        minpos = obj2.index(min(obj2))
        w.iloc[i] = solution[minpos]
        print("....................................................")
        # print("min pos TC is {}".format(minpos))
        # print(solution)
        # print(obj1, obj2, solution[minpos])
        print(w)
        print(".....................................................")
    return w
result = strategy(s)
