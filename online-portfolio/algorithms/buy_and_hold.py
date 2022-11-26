
def strategy(s):
    """
    Description: Buy equal amount of each stock in the beginning and hold them forever.
    :parameter
    :param s: Initial dataframe

    :return matrix weights
    """
    w = s * 0
    for i in range(1, len(s)):
        for j in range(len(s.columns)):
            w.iloc[i, j] = 1 / len(s.columns)
    return w

