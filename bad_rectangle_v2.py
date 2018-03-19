"""
bad_rectangle version 1
http://mathworld.wolfram.com/AlcuinsSequence.html
https://archive.lib.msu.edu/crcmath/math/math/a/a104.htm
https://en.wikipedia.org/wiki/Alcuin%27s_sequence
https://en.wikipedia.org/wiki/Nearest_integer_function
"""

n = int(input())
counter = 0
if n % 2 == 0:
    counter = int(round((n**2)/48))
else:
    counter = int(round(((n+3)**2)/48))
print(counter)

