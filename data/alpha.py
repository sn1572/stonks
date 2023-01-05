#!/usr/bin/env  python3
import pandas as pd
import pandas_datareader as pdr


_api_key = '7OS4EM4E4RVMS47B'


def sample():
    ts = pdr.av.time_series.AVTimeSeriesReader('IBM', api_key = _api_key)
    df = ts.read()
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    df[['open', 'close']].plot()


if __name__ == '__main__':
    sample()
