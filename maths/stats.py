import numpy as np
from functools import reduce


def var(v):
    ''' quick n' dirty statistical variance '''
    mu = reduce(lambda x,y: x+y, v)
    mu /= len(v)
    var = reduce(lambda x,y: x+(y-mu)**2, v)
    var /= len(v)
    return var


def covar(u, v):
    ''' quick n' dirty statistical covariance '''
    assert len(u) == len(v)
    summer = lambda x,y: x+y
    mu_u = reduce(summer, u) / len(u)
    mu_v = reduce(summer, v) / len(v)
    both = zip(u,v)
    cov = reduce(lambda x,y: (x[0]+(y[0]-mu_u)*(y[1]-mu_v), 0), both)
    return cov[0] / len(u)


def beta(stonk, snp):
    return covar(stonk, snp) / var(snp)


def capm(stonk, dividend_yield, snp, rfr, exp):
    '''
    Args:
      stonk: Vector of stonk data.
      dividend_yield: What it says on the tin.
      snp: Vector of snp 500 data over the same term as stonk.
      rfr: Risk-free rate.
      exp: Expected growth of the market (eg. 8% per year or whatever).
    '''
    s_beta = beta(stonk, snp)
    expected_return = dividend_yield + s_beta * (exp - rfr)
    return expected_return
