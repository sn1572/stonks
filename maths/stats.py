import numpy as np
from functools import reduce


def var(v):
    ''' quick n' dirty statistical variance '''
    mu = reduce(lambda x,y: x+y, v)
    mu /= len(v)
    v[0] = (v[0]-mu)**2
    var = reduce(lambda x,y: x+(y-mu)**2, v)
    var /= (len(v) - 1)
    return var


def covar(u, v):
    ''' quick n' dirty statistical covariance '''
    assert len(u) == len(v)
    summer = lambda x,y: x+y
    mu_u = reduce(summer, u) / len(u)
    mu_v = reduce(summer, v) / len(v)
    cov = 0
    for x, y in zip(u,v):
        cov += (x-mu_u)*(y-mu_v)
    return cov / (len(u)-1)


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
