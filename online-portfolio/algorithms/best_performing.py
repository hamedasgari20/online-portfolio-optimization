def strategy(s):
    """
    Description: This strategy invests in the coin with the highest return at each stage
    :parameter
    :param s: Initial dataframe

    :return matrix weights
    """
    r = (s / s.shift(1)) - 1
    highest_return_symbol = r.idxmax(axis=1).shift(1)
    # construct weights
    w_mom = s * 0
    for col in r.columns:
        w_mom.loc[highest_return_symbol == col, col] = 1
    return w_mom
