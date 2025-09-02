def odd_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False


def avg(list):
    return sum(list)/len(list)


def max(list):
    m = 0
    for i in list:
        if m < i:
            m = i
    return m


def min(list):
    m = list[0]
    for i in list:
        if m > i:
            m = i
    return m
