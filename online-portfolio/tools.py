import numpy as np
import pandas as pd
import pandas_datareader.data as web

coin_list = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD", "SOL-USD", "DOGE-USD", "MATIC-USD", "DOT-USD", "TRX-USD"]
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
    # loading data in chunks from Yahoo is more robust than loading everything at once
    for i, chunk in enumerate(np.array_split(list_of_coins, 5)):
        print(f'Loading chunk {i}')
        s.append(web.DataReader(chunk, source_of_data, start=start_from, end=end_to)['Adj Close'])
    s = pd.concat(s, axis=1)
    s.to_csv(f'data/data from {start_from} to {end_to}.csv', index=False)
