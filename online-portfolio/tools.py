import numpy as np
import pandas as pd
import pandas_datareader.data as web

coin_list = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD"]
start_time = '2021-01-01'
end_time = '2021-10-27'
data_source = 'yahoo'


def get_data(list_of_coins: list, start_from: str, end_to: str, source_of_data: str):
    """
    :parameter
    :param list_of_coins: list          for example: ["BTC-USD", "ETH-USD", "BNB-USD"]
    :param start_from: string          for example: '2018-01-01'
    :param end_to: string              for example: '2021-08-17'
    :param source_of_data: string      for example: 'yahoo'

    :return dataframe which includes daily close price
    """
    s = []
    # loading datasets in chunks from Yahoo is more robust than loading everything at once
    for i, chunk in enumerate(np.array_split(list_of_coins, 5)):
        print(f'Loading chunk {i}')
        s.append(web.DataReader(chunk, source_of_data, start=start_from, end=end_to)['Adj Close'])
    s = pd.concat(s, axis=1)
    s.to_csv(f'datasets/data from {start_from} to {end_to}.csv', index=False)


# get_data(list_of_coins=coin_list, start_from=start_time, end_to=end_time, source_of_data=data_source)


def rate_of_return(s):
    """
    Description: This function calculates the rate of return for dataframe
    :parameter
    :param s: Initial dataframe

    :return rate of return dataframe
    """
    r = (s / s.shift(1)) - 1
    return r


def transaction_cost(w, alfa):
    """
    Description: This function calculates the transaction cost for matrix weight
    :parameter
    :param w: matrix weight and transaction fee for each trade
    :param alfa: transaction fee for each trade

    :return transaction cost percentage of the initial deposit
    """
    TC = 0
    for i in range(len(w) - 1):
        for j in range(len(w.columns)):
            TC = TC + abs(w.iloc[i, j] - w.iloc[i + 1, j])
    return TC * alfa


def portfolio_return(w, r):
    """
    Description: This function calculates the portfolio return for matrix weight
    :parameter
    :param w: matrix weight
    :param r: matrix rate of return

    :return portfolio return percentage of the initial deposit
    """
    multi = w.mul(r)
    return multi.sum().sum()


def sortino_ratio(w, r, risk_free_rate):
    """
    Description: This function calculates the sortino ratio for matrix weight
    :parameter
    :param w: matrix weight
    :param r: matrix rate of return
    :param risk_free_rate: risk free rate percentage

    :return portfolio sortino ratio
    """
    # todo sortino ratio get inf
    multi = w.mul(r)
    std_neg = multi[multi < 0].std()
    a = multi.sum().sum()-risk_free_rate
    b = a / std_neg.sum()
    return b


