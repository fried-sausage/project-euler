import itertools as it

def gen1():
    yield 2
    primes = set()
    steps = 0, 0, 0
    for n in it.count(start=3, step=2):
        if steps[0] == 3:
            steps[0] = 1
        else:
            for p in primes:
                if n%p == 0:
                    break
            else:
                primes.add(n)
                yield n
            steps += 1

def count_until(generator, num):
    for i in generator():
        if i>num: break
        pass

"""
2 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 32 33
  0 1 2 3 .1 .2 .3 .1 .2 .3 .1 .2 .3 .1 .2 .3 .1
    0 1 2 .3 .4 .5 .1 .2 .3 .4 .5 .1 .2 .3 .4 .5
      0 1 .2 .3 .4 .5 .6 .7 .1 .2 .3 .4 .5 .6 .7
"""