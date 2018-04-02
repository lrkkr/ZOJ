# IticoMilk
import sys


def conflict(n, m, i):

    pass


def reduce_num(n):
    n_list = []
    if n > 100:
        y = 101
    else:
        y = n + 1
    for i in range(1, y):
        if n % i == 0:
            n_list.append(i)
    print n_list
    return n_list


def solve(n, m):
    n_list = reduce_num(n)
    m_list = reduce_num(m)
    i = list(set(n_list[1:]) & set(m_list[1:]))
    conflict(n, m, i)
    print i
    print '****************'


for line in sys.stdin:
    a = line.split()
    solve(int(a[0]), int(a[1]))
