# a = lambda x: x + 3
# print(a(10))
# b = lambda c, d: (c + d)**2
# print(b(11, 2))
# e = lambda f, g: (f**2 + 2 * g)
# print(e(2, 3))
# h = lambda i, j: (3 * (i*2) + 4 * j + 4)
# print(h(2, 3))
# k = lambda l, m: 3*(l * 3) + 4*(l*2) + 3*m + 10
# print(k(2, 4))
# n = [12, 9, 3, 7, 5, 4, 6, 8, 10, 24]
# o = list(map(lambda x: (x**2), n))
# print(o)
# p = [12, 9, 3, 7, 5, 4, 6, 8, 10, 24]
# q = list(filter(lambda x: (x**3 <= 100), p))
# print(q)
# r = [12, 9, 3, 7, 5, 4, 6, 8, 10, 24]
# s = list(map(float, r))
# print(s)
from functools import reduce
# t = [12, 9, 3, 7, 5, 4, 6, 8, 10, 24]
# u = reduce(lambda v, w: v+w, t)  # returns a single value eg the sum in this case
# print(u)
# y = ['jer', 'si', 's']
# z = reduce(lambda aa, bb: aa+bb, y)
# print(z)
