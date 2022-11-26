
def strategy(s):
    """
    Description: This strategy invests in the coin with the lowest return at each stage
    :parameter
    :param s: Initial dataframe

    :return matrix weights
    """
    r = (s / s.shift(1)) - 1
    lower_return_symbol = r.idxmin(axis=1).shift(1)
    # construct weights
    w_rev = s * 0
    for col in r.columns:
        w_rev.loc[lower_return_symbol == col, col] = 1
    return w_rev