"""Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

limit = 4*10**6

def fib_even():
    a, b = 0, 1
    while True:
        yield a
        a, b = a+2*b, 2*a + 3*b

def take(generator, max_num):
	gen = generator()
	for i in gen:
		if i>max_num:
			break
		yield i

ans = sum(take(fib_even, limit))

print(ans)