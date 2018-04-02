# IticoMilk
import sys


def scores(n_list):
    pass


def reduce_num(n):
    n_list = []
    if n == 1:
        return [1]
    while n not in [1]:
        for i in xrange(2, n + 1):
            if n % i == 0:
                n /= i
                if n == 1:
                    n_list.append(i)
                    print n_list
                    return n_list
                else:
                    n_list.append(i)
                break


def solve(n, m):
    n_list = reduce_num(n)
    m_list = reduce_num(m)


for line in sys.stdin:
    a = line.split()
    solve(int(a[0]), int(a[1]))
