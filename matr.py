from math import gcd 
import sympy
import random

random.seed(1)

def is_valid_2x2(a,b,c,d):
    det = a*d - c*b 
    if gcd(det%26,26) == 1 :
        return True
    else :
        return False



def is_valid(K):
    det = sympy.Matrix(K).det()
    return gcd(det%26,26)==1 

def samples(n,x):
    valid = 0 
    for i in range(x):
        K = []
        for j in range(n):
            K.append([random.randint(0, 25) for p in range(n)])
        if is_valid(K):
            valid += 1 
    print(valid/x)


for i in range(2,6):
    samples(i,100000)