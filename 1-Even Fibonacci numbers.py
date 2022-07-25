
#Even Fibonacci numbers

ans=[1,]
toplami=0

x=1
y=2
while x<=4000000:
    ans.append(y)
    x,y = y, x + y

for i in ans:
    if i%2 == 0:
        toplami += i

print(ans)
print(toplami)
