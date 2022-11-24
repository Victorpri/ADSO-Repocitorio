


n = 6

for n in range (1, 1001):
     s = 0

for i in range (1, n):
             if n % i == 0:
                  print('divisor', i)
             else:
                  print('no divisor', i)
             s = s + i

if  s == n:
    print('perfecto')
else:
    print('no perfecto')
    


