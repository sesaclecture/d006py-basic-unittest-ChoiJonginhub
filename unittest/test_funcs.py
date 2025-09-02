# TODO: 사용자 모듈 import
from main_funcs import odd_even, max, min, avg

data = [1, 2, 3, 4, 10, 11]


def test_always():
    assert True is odd_even(2)
    assert False is odd_even(11)

    assert 31/6 == avg(data)
    assert 11 == max(data)
    assert 1 == min(data)
