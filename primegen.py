import itertools

def gen1():
    yield 2
    primes = set()
    step = 0
    for n in itertools.count(start=3, step=2):
        if step == 3:
            step = 1
        else:
            for p in primes:
                if n%p == 0:
                    break
            else:
                primes.add(n)
                yield n
            step += 1

"""
As for now we are skipping all numbers that are even
or divisible by 3. There is a way to do it more
efficiently, changin length of our 'steps' as we
discover new primes.
Some observations:
2 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 32 33
  0 1 2 3 .1 .2 .3 .1 .2 .3 .1 .2 .3 .1 .2 .3 .1
    0 1 2 .3 .4 .5 .1 .2 .3 .4 .5 .1 .2 .3 .4 .5
      0 1 .2 .3 .4 .5 .6 .7 .1 .2 .3 .4 .5 .6 .7
"""

def count_until(stop, generator=gen1):
    for i in generator():
        if i >= stop:
            break
        yield i

if __name__ == '__main__':
    for i in count_until(1000):
        print(i, end = ' ')
    print()

