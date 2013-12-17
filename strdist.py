#!/usr/bin/env python3

# source : http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_subsequence

import argparse

def main():

    parser = argparse.ArgumentParser(description='lib for the length of the'\
            ' longuest common subsequence between 2 strings.')



    parser.add_argument(
            '-t',
            '--test',
            help='run the doctest suites and exit',
            action = 'store_true'
            )


    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()

    return


def LCS(X, Y):
    m = len(X)
    n = len(Y)
    C = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
    if C[i][j-1] >= C[i-1][j]:
        R.update(backTrackAll(C, X, Y, i, j-1))
    if C[i-1][j] >= C[i][j-1]:
        R.update(backTrackAll(C, X, Y, i-1, j))
    return R

def longest_sub_len(X,Y):
    """ Returns the length of the longuest common subsequence between string
    X and Y.

    EXAMPLE
    =======

    >>> longest_sub_len("New_York_City","New York")
    7

    """

    len_x = len(X)
    len_y = len(Y)

    C = LCS(X, Y)
    longest_length = C[len_x][len_y]

    return longest_length

if __name__ == '__main__':
    main()

