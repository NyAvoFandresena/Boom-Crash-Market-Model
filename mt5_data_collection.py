#this file handles data collection from MT5 to pandas DataFrame

import MetaTrader5 as mt5
import pandas as pd

def create_lag_features(data, lags=5):
    for lag in range(1, lags + 1):
        data[f'lag_{lag}'] = data['close'].shift(lag)
    return data.dropna()

mt5.initialize()
symbol = "Boom 500"
data = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 1000)
raw_data = pd.DataFrame(data)
mt5.shutdown()

data_frame = create_lag_features(raw_data)