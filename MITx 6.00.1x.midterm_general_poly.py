def general_poly(L):
    def formula(x):
        n = 0
        for i in L:
            n = x * n + i
        return n
    return formula
