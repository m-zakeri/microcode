"""
bad_rectangle version 1
This version not work yet!

"""
n = 12
counter = 0
# if n % 3 == 0:
    # print(n//3, n//3, n//3)
    # counter += 1
for a in range(1, n-1):
    b = a
    c = n - (a+b)
    if a+b < c:
        continue
    else:
        if a + b > c and a + c > b and b + c > a:
            print(a, b, c)
            counter += 1
        while b < c:
            b += 1
            c = n - (a+b)
            if a+b > c and a+c > b and b+c > a:
                print(a, b, c)
                counter += 1

print(counter)
