#!/usr/bin/env  python3
import yfinance as yf
import matplotlib.pyplot as plt


def sample():
    data = yf.download('INTC', '2021-01-01', '2021-09-30')
    data["Close"].plot()
    plt.show()


if __name__ == '__main__':
    sample()
