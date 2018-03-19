"""
https://projecteuler.net/problem=36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
count = 0
for i in range(1000000):
    integer = str(i)
    integer_reverse = integer[::-1]
    binary = "{0:b}".format(i)
    binary_reverse = binary[::-1]
    if binary == binary_reverse and integer == integer_reverse:
        count += i
print(count)


