#!/usr/bin/env  python
import sys
sys.path.insert(0, '..')
import os
from maths import stats
import yfinance as yf
import matplotlib as plt
import pickle


def get_data():
    intc = yf.download(['INTC', 'SPY'], '2021-01-01', '2023-01-02')
    with open('saved.pkl', 'wb') as f:
        pickle.dump(data, f)


def load_data():
    save_file = os.path.join(os.path.dirname(__file__), 'saved.pkl')
    if not os.path.exists(save_file):
        get_data()
    with open(save_file, 'rb') as f:
        data = pickle.load(f)
    return data


def main():
    data = load_data()
    intc = data[('Close', 'INTC')]
    snp = data[('Close', 'SPY')]
    print(f"Intel Beta: {stats.beta(intc, snp)}")
    exp = 0.00
    rfr = 0.0369
    print(f"CAPM with expected growth {exp} and risk free rate {rfr}:")
    print(stats.capm(intc, 0.0531, snp, rfr, exp))


if __name__ == '__main__':
    main()
