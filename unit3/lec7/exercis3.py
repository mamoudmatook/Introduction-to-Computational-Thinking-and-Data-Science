def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np
    if len(L) == 0:
        return float('NaN')
    else:
        return np.std([i for i in map(len, L)])
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
