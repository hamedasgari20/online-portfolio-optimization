from utils import *


def strategy(s):
    w = s * 0
    for i in range(1, len(s)):
        # for each row in matrix s find nsga2 result
        # and save it in w
        w[i] = nsga2(s, i, w)
    return w
