from utils import *


s = pd.read_csv('../datasets/test_data_1.csv')
r = (s / s.shift(1)) - 1


def strategy(s):
    w = s * 0
    for i in range(1, len(s)):
        # for each row in matrix s find nsga2 result and save it in w
        solution = []
        obj1, obj2, solution = nsga2(s, w.iloc[i-1, :], r.iloc[i, :], i, population=3, max_gen=10)
        # print(solution)
        # # In each step pareto layer can seen we two lines below
        # non_dominating_curve_plotter(obj1, obj2)

        # TODO find similar w with previous w between best solution found solution[0] is not correct
        minpos = obj2.index(min(obj2))
        w.iloc[i] = solution.iloc[minpos, :]


    return w
result = strategy(s)
print(result)