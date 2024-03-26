import sys
sys.set_int_max_str_digits(0)

a = []

number = int(input())

def checkPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return 0
    return 1

def divisor(x):
    temp = x
    while temp <= number:
        temp = temp * x
    return temp / x

for i in range(2,number+1):
    if checkPrime(i) == 1:
        a.append(i)
    
res = 1
for x in a:
    div = divisor(x)
    # print(div)
    res = res * int(div)

resStr = str(int(res))
print(resStr)
# print()
# print(len(resStr))

# sub_lists = [resStr[i:i+3] for i in range(1, len(resStr), 3)]
# print(sub_lists)
