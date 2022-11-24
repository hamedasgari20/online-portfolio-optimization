
def worst_performing_strategy(S):
    # todo rate_of_return function must be imported here
    R = (S / S.shift(1)) - 1
    lower_return_symbol = R.idxmin(axis=1).shift(1)
    # construct weights
    W_rev = S * 0
    for col in R.columns:
        W_rev.loc[lower_return_symbol == col, col] = 1
    return W_rev