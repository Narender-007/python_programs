# find python prime number
# find third largest number
# find palindrome "ramkmar"
# find fibanacci series 
# find reverse string "atoz"
# find factorial number
# find fizz and buzz
# convert to farenhit
# python patterns

# find python prime number
n = 97
for i in range(2,n):
    if (n % i)==0:
        v = "thi is not prime number",n
        break
    else:
        v = "this is the prime number",n
print(v)
a = 0
b = 0
c = 0
h = [2,5,7,3,7,1,3,9,78,34,89,23,0]

# find third largest number
sortt = h.sort()
print(h)

for i in h:
    if i > a:
        c = b
        b = a
        a = i
    elif i>b and i!=a:
        c=b
        b=i
    elif i>c and i!=b and i!=a:
        c=i
        
print(a,b,c)

# find palindrome "ramkmar"
c = "mangnam meangnam"
print(c[::-3])
print(c == c[::-1])

# find fibanacci series 
a=0
b = 1
n =10
l = []
while a<n:
    l.append(a)
    
    a = a+b
    a,b = b,a 

print(l)

# find reverse string "atoz"
n = "narender"
print(n[::-1])

# find fizz and buzz
a = "Fizz"
b = "Buzz"
c = "FizzBuzz"
n = 15
for i in range(1,n+1):
    if i%3==0 and i%5 ==0:
        print(c)
    elif i%3 == 0:
        print(a)
    elif i%5 == 0:
        print(b)
    else:
        print(i)

# find factorial number
def factorial(n):
    if n == 0:
        print("this is not factorial")
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

c = factorial(5)
print(c)

# python patterns
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
        
    print()
