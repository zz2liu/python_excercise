def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_all(n):
    res = [fib(i) for i in range(n)]
    return res

def fib_all_dynamic(n):
    res = []
    for i in range(n):
        if i<2:
            res.append(i)
        else:
            res.append(res[i-2] + res[i-1])
    return res

if __name__ == '__main__':
#    import timeit
#    timeit.timeit('print(fib_all(20))', number=1, setup='from __main__ import fib_all')
    import IPython
    ipy = IPython.get_ipython()
    #ipy.magic("time fib_all(20)")
    ipy.magic("timeit fib_all(20)")
    ipy.magic("timeit fib_all_dynamic(20)")
#%time print(fib_all_dynamic(20))
