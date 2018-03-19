import math
x =  600851475143
"""l = []
for i in range(2, int(x/2)):
    flag = True
    for j in range(2,round(math.sqrt(i)),2):
        if i%j == 0:
            flag = False
            break
    if flag:
        l.append(i)

# print(l)

for i in range(1, len(l)):
    if x%l[-i] == 0:
        print(l[-i])
        break
"""
num = 600851475143
i = 2
while i * i < num:
    while num % i == 0:
        num = num / i
    i = i + 1
print(num)
