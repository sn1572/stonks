import sys
sys.path.insert(0, '..')
import stats
import pytest


def test_covar():
    x = [2.1, 2.5, 3.6, 4.0]
    y = [8,10,12,14]
    assert stats.covar(x,y) == pytest.approx(2.267, 1e-3)


def test_var_covar_equal():
    x = [2.1, 2.5, 3.6, 4.0]
    assert stats.covar(x,x) - stats.var(x) == pytest.approx(0, 1e-5)
