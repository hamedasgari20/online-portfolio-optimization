import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt



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
    return -b


def objective2(w_prev, w_new):
    w_prev = pd.Series(w_prev.values)
    w_new = pd.Series(w_new.values)

    TC = 0
    for i in range(len(w_new)):
        TC = TC + abs(w_prev.iloc[i] - w_new.iloc[i])
    return TC


def non_dominated_sorting_algorithm(values1, values2):
    S = [[] for i in range(0, len(values1))]
    front = [[]]
    n = [0 for i in range(0, len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0, len(values1)):
        S[p] = []
        n[p] = 0
        for q in range(0, len(values1)):
            if (values1[p] > values1[q] and values2[p] > values2[q]) or (
                    values1[p] >= values1[q] and values2[p] > values2[q]) or (
                    values1[p] > values1[q] and values2[p] >= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q] > values1[p] and values2[q] > values2[p]) or (
                    values1[q] >= values1[p] and values2[q] > values2[p]) or (
                    values1[q] > values1[p] and values2[q] >= values2[p]):
                n[p] = n[p] + 1
        if n[p] == 0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while (front[i] != []):
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] = n[q] - 1
                if (n[q] == 0):
                    rank[q] = i + 1
                    if q not in Q:
                        Q.append(q)
        i = i + 1
        front.append(Q)
    del front[len(front) - 1]
    return front

def index_locator(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1

def sort_by_values(list1, values):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_locator(min(values),values) in list1:
            sorted_list.append(index_locator(min(values),values))
        values[index_locator(min(values),values)] = math.inf
    return sorted_list



def crowding_distance(values1, values2, front):
    distance = [0 for i in range(0,len(front))]
    sorted1 = sort_by_values(front, values1[:])
    sorted2 = sort_by_values(front, values2[:])
    distance[0] = 9999999999999999
    distance[len(front) - 1] = 9999999999999999
    for k in range(1,len(front)-1):
        distance[k] = distance[k]+ (values1[sorted1[k+1]] - values2[sorted1[k-1]])/(max(values1)-min(values1))
    for k in range(1,len(front)-1):
        distance[k] = distance[k]+ (values1[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
    return distance


def crossover(a,b, s):
    r=random.random()
    if r>0.5:
        return mutation((a+b)/2, s)
    else:
        return mutation((a-b)/2, s)


def mutation(solution, s):
    mutation_prob = random.random()
    if mutation_prob <1:
        solution = initial_solution(1, s)
    return solution


def non_dominating_curve_plotter(objective1_values, objective2_values):
    plt.figure(figsize=(15,8))
    objective1 = [i * -1 for i in objective1_values]
    objective2 = [j * -1 for j in objective2_values]
    plt.xlabel('Objective Function 1', fontsize=15)
    plt.ylabel('Objective Function 2', fontsize=15)
    plt.scatter(objective1, objective2, c='red', s=25)
    plt.show()


def nsga2(s, w, r, i,  population, max_gen):

    gen_no = 0
    solution = initial_solution(population, s)
    while (gen_no < max_gen):
        # print(solution)
        objective1_values = [objective1(solution.loc[j, :], r) for j in range(0, population)]
        objective2_values = [objective2(w, solution.loc[k, :]) for k in range(0, population)]
        # print(objective2_values)
        # print('ok')
        # objective1_values = [float(i) / sum(objective1_values_un_normal) for i in objective1_values_un_normal]
        # objective2_values = [float(i) / sum(objective2_values_un_normal) for i in objective2_values_un_normal]


        non_dominated_sorted_solution = non_dominated_sorting_algorithm(objective1_values[:], objective2_values[:])
        # print('Best Front for Generation:', gen_no)
        # for values in non_dominated_sorted_solution[0]:
        #     print(values)
        #     print(round(solution.iloc[values, :], 3), end=" ")
        # print("\n")


        crowding_distance_values = []
        for i in range(0, len(non_dominated_sorted_solution)):
            crowding_distance_values.append(
                crowding_distance(objective1_values[:], objective2_values[:], non_dominated_sorted_solution[i][:]))
        solution2 = solution[:]

        while (len(solution2) != 2 * population):
            a1 = random.randint(0, population - 1)
            b1 = random.randint(0, population - 1)
            res_cross_over = crossover(solution.iloc[a1, :], solution.iloc[b1, :], s)
            solution2 = solution2.append(res_cross_over, ignore_index=True)
        objective1_values2 = [objective1(solution2.loc[i, :], r) for i in range(0, 2 * population)]
        objective2_values2 = [objective2(w, solution2.loc[i, :]) for i in range(0, 2 * population)]
        # print(objective2_values2)
        non_dominated_sorted_solution2 = non_dominated_sorting_algorithm(objective1_values2[:], objective2_values2[:])
        crowding_distance_values2 = []
        for i in range(0, len(non_dominated_sorted_solution2)):
            crowding_distance_values2.append(
                crowding_distance(objective1_values2[:], objective2_values2[:], non_dominated_sorted_solution2[i][:]))
        new_solution = []
        for i in range(0, len(non_dominated_sorted_solution2)):
            non_dominated_sorted_solution2_1 = [
                index_locator(non_dominated_sorted_solution2[i][j], non_dominated_sorted_solution2[i]) for j in
                range(0, len(non_dominated_sorted_solution2[i]))]
            front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
            front = [non_dominated_sorted_solution2[i][front22[j]] for j in
                     range(0, len(non_dominated_sorted_solution2[i]))]
            front.reverse()
            for value in front:
                new_solution.append(value)
                if (len(new_solution) == population):
                    break
            if (len(new_solution) == population):
                break
        solution = [solution2.iloc[i, :] for i in new_solution]
        obj1 = [objective1(solution[j], r) for j in range(0, population)]
        obj2 = [objective2(w, solution[k]) for k in range(0, population)]
        # todo this solution must be return as final solution in each iteration
        gen_no = gen_no + 1
    return [obj1, obj2, solution]



