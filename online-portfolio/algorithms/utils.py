import pandas as pd
import numpy as np
import math
# test import
s = pd.read_csv('../datasets/test_data_1.csv')
w = s * 0

def initial_solution(population, s):
    sol = pd.DataFrame(np.random.randint(0,100,size=(population, len(s.columns))))
    sol = sol.div(sol.sum(axis=1), axis=0)
    return sol


def objective1(w, r):
    w = pd.Series(w.values)
    r = pd.Series(r.values)
    multi = w.mul(r, fill_value=0)
    std_neg = multi[multi < 0].std()
    a = multi.sum()
    if math.isnan(std_neg):
        b = a
    else:
        b = a / std_neg
    return b


def objective2(w_prev, w_new):
    w_prev = pd.Series(w_prev.values)
    w_new = pd.Series(w_new.values)

    TC = 0
    for i in range(len(w_new)):
        TC = TC + abs(w_prev.iloc[i] - w_new.iloc[i])
    return TC


def nsga2(s, w, i,  population, max_gen):
    r = (s / s.shift(1)) - 1
    gen_no = 0
    solution = initial_solution(population, s)
    while (gen_no < max_gen):
        print(solution)
        print(solution.loc[i, :])
        print(w.loc[i-1, :])
        objective1_values = [objective1(solution.loc[j, :], r.loc[j, :]) for j in range(0, population)]
        objective2_values = [objective2(w.loc[i-1, :], solution.loc[k, :]) for k in range(0, population)]

        print(objective1_values, objective2_values)



        gen_no = gen_no + 1
    return solution



# for test
w = nsga2(s, w, i=1, population=3, max_gen=1)
print(w)