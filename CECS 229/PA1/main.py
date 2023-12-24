#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229: Programming Assignment #1
# 
# #### Due Date: 
# 
# Sunday, 2/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment, you must submit **to CodePost** this file converted to a Python script named `pa1.py`
# 
# #### Objectives:
# 
# 1. Compute the quotient and remainder of two numbers.
# 2. Apply numerical algorithms for computing the sum of two numbers in binary representation.
# 3. Apply numerical algorithms for computing the modular exponentiation of a positive integer.
# 
# 
 
# --------------------------------
# 
# #### Problem 1:
# 
# Program a function `div_alg(a, d)` that computes the quotient and remainder of $$a \div d$$ according to the Division Algorithm (THM 4.1.2).   
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - an integer representing the dividend
#     * `d` - positive integer representing the divisor
# 
#     
# 2. OUTPUT:
#     * a dictionary of the form `{'quotient' : q, 'remainder' : r}` where `q` and `r` are the quotient and remainder values, respectively.  The remainder should satisfy, $0 \leq r < d$.
# 
#  
# EXAMPLE: 
# 
# `>> div_alg( 101 , 11 )`
# 
# `{'quotient' : 9, 'remainder' : 2}`
 
# In[12]:
 
 
def div_alg(a: int, d: int):
    q = 0
    r = abs(a)
    
    while r >= d:         # While 'remainder' (what's left) is greater than
        r -= d            # the divisor
        q += 1
    if a < 0 and r > 0:   # If dividend was negative
        r = d - r
        q = -(q + 1)
    return {'quotient':q, 'remainder':r}
 
 
# --------------------------------
# 
# #### Problem 2:
# 
# Program a function `binary_add(a, b)` that computes the sum of the binary numbers  $$a = (a_{i-1}, a_{i-2}, \dots, a_0)_2$$ and $$b = (b_{j-1}, b_{j-2}, \dots, b_0)_2$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  The function can not use built-in functions that already perform some kind of binary representation or addition of binary numbers.  For example, the function implementation can **not** use the functions `bin()` or `int(a, base=2)`.
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
#     * `b` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
# 
#     
# 2. OUTPUT:
#     * the string of 0's and 1's that is the result of computing $a + b$.  The string must be separated by spaces into blocks of 4 characters or less, beginning at the end of the string.
# 
#  
# EXAMPLE: 
# 
# `>> binary_add( '10 1011' , '11011')`
# 
# `'100 0110'`
# 
# 
# 
 
# In[15]:
 
 
def binary_add(a: str, b: str):
    # Strips spaces
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # Makes strings the same length, append 0's to front
    if len(a) is not len(b):
        diff = abs(len(a) - len(b))
        if len(a) < len(b):
            a = '0' * diff + a
        else:
            b = '0' * diff + b
    
    total = ''
    carry = 0
    
    # LSB to MSB
    for i in range(len(a) - 1, -1, -1):
        
        bit_sum = (int(a[i]) + int(b[i]) + carry) % 2
        carry = (int(a[i]) + int(b[i]) + carry) // 2
        
        total = str(bit_sum) + total
    
    if carry == 1:
        total = str(carry) + total
    
    split = len(total) // 4
    if len(total) % 4 == 0:
        split -= 1
        
    # Divides bit-string into chunks of four
    loc = len(total) - 4
    for k in range(split):
        total = total[:loc] + ' ' + total[loc:]
        loc -= 4
    
    return total
 
 
# --------------------------------
# 
# #### Problem 3:
# 
# Program a function `mod_exp(b, n, m)` that computes $$b^n \mod m$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  For example, if the function implementation simply consists of `b ** n % m`, no credit will be given.  
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `b` - positive integer representing the base
#     * `n` - positive integer representing the exponent
#     * `m` - positive integer representing the modulo
# 
#     
# 2. OUTPUT:
#     * the computation of $b^n \mod m$ if b, n, m are positive integers, 0 otherwise.
# 
#  
# EXAMPLE: 
# 
# `>> mod_exp( 3 , 644, 645 )`
# 
# `36`
# 
# 
# 
 
# In[14]:
 
 
def mod_exp(b: int, n: int, m: int):
    
    if b < 1 or m < 1 or n < 1:
        return 0
    
    # Converts n into binary
    quotient = n
    bit_num = 0
    bit_n = ''
    while quotient != 0:
        bit_n = str(quotient % 2) + bit_n
        quotient = quotient // 2
        bit_num += 1
    
    x = 1
    power = b % m
    for i in range(len(bit_n) - 1, -1, -1):
        if int(bit_n[i]) == 1:
            x = (x * power) % m
        power = (power ** 2) % m
    
    return x
 