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



a = input("enter:")#enter:abc-d
a1 = list(a)
print(a1)
c = []
for i in a1:
    if i == "-":
        v1 = a1.index(i)
        special_chararcter = "-"
    else:
        c.append(i)

v2 = "".join(c)
v3 = v2[::-1]
v4 = list(v3)
v4.insert(v1,special_chararcter)
print(v4)
v4 = "".join(v4)
print(v4)       # dcb-a


# Problem Name is &&& Is Power of 10 &&& PLEASE DO NOT REMOVE THIS LINE.

"""
 Instructions to candidate.
  1) Run this code in the REPL to observe its behaviour. The
     execution entry point is main().
  2) Consider adding some additional tests in doTestsPass().
  3) Implement isPowerOf10() correctly.
  4) If time permits, some possible follow-ups.
"""

def isPowerOf10(x):
        """ Returns True if x is a power-of-10. Otherwise returns False. """
        # todo: implement here
        i = 1
        if x > 1:
            while i < x:
                i *= 10
        elif x > 0:
            while i > x:
                i /= 10.

        if i == x:
            return True
        return False
        

def doTestsPass():
        """ Returns True if all tests pass. Otherwise returns False. """
        # todo: implement more tests, please
        # feel free to make testing more elegant
        doPass        = True
        powersOf10    = [1,10,100,100000, .1, .001]
        notPowersOf10 = [5,0,-10,20,110,10100,42]

        for n in powersOf10:
                if not isPowerOf10(n):
                        print("Failed for " + str(n) + "\n")
                        doPass = False


        for n in notPowersOf10:
                if isPowerOf10(n):
                        print("Failed for " + str(n) + "\n")
                        doPass = False

        if doPass:
                print("All tests pass\n")

        return doPass


if __name__ == "__main__":
        doTestsPass()




# interview question

a = [1,2,3,4,11,12,13,21,22,23,31,41,42]

# c = {(1,2,3,4):4,(11,12,13):3,(21,22,23):3,(31):1}

dict_data = {}
len_list = len(a)
seq_list = []
print(a[-1])
for row in range(1,a[-1]+2):
    # print(row)
    if row in a:
        seq_list.append(row)
    else:
        tuple_data = tuple(seq_list)
        if len(seq_list)>0:
            dict_data[tuple_data] = len(seq_list)
        seq_list=[]
    
print(dict_data)


# def fibonacci_series(n):
    
#     for i in range(n):
#         v = n*i
#         print(v)
        
#     return fibonacci_series(n-1)
    
# n = int("enter the numebr:")    
# v = fibonacci_series(n)
        
# Design a Python class that acts as a simple key-value store with the following operations:
 
# set(key, value): Sets the given key to the value.
# get(key): Returns the value associated with the key, or None if the key doesn't exist.
# delete(key): Deletes the key and its associated value.
# Challenge: Implement the class ensuring efficient get, set, and delete operations.

class A:
    dict_data = {}
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    def set_method(self):
        dict_data['name'] = self.name
        dict_data['age'] = self.age
        print("dictionary prepared")
        
    def get_method(self):
        for key, value in dict_data.items():
            if value == None:
                pass
            else:
                print("without none values are printed")
                print(dict_data[key])
                
    def delete_method(self,name):
        if name:
            dict_data.remove(name)
            
class_name = A("narender",28)
m1 = class_name.set_method()
m2 = class_anme.get_method()
m3 = class_name.delete_method("narender")

# Question: Implement a Flask application that serves an API endpoint /calculate which accepts POST requests with JSON data containing a list of integers. The endpoint should return the median of the integers in the list. If the list has an even number of integers, return the average of the two middle numbers.
# Question:
# Implement a Flask application with two endpoints:
 
# /upload accepts a POST request with a file upload.

from flask import Falsk, JsonResponse


app = Flask(__name__)

@app.post("")
