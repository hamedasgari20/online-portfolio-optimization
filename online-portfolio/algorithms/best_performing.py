
def highest_performing_strategy(S):
    R = S / S.shift(1)
    highest_return_symbol = R.idxmax(axis=1).shift(1)
    # construct weights
    W_mom = S * 0
    for col in R.columns:
        W_mom.loc[highest_return_symbol == col, col] = 1
    return W_mom