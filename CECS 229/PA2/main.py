#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229: Programming Assignment #2
# 
# #### Due Date: 
# 
# Sunday, 2/19 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa2.py`
# 
# #### Objectives:
# 
# 1. Use the Sieve of Eratosthenes to find all primes in a given range.
# 2. Design a computational algorithm for finding the Bézout coefficients of two integers.
# 3. Use Bézout coefficients to calculate the GCD.
# 
 
# -------------------------------------------------------
# #### Problem 1:
# 
# Create a function `primes(a, b)` that uses the Sieve of Eratosthenes to find all the primes $p$ satisfying $a \leq p \leq b$.  You may not use any built-in functions that perform entire or part of this algorithm.
# 
# 1. INPUT:
#   
#   * `a` - a positive integer greater than or equal to 1 (raise a `ValueError` if an integer less than 1 is given), that is the lower bound
#   * `b` - a positive integer greater than or equal to `a` (raise a `ValueError` if `b` < `a`)
#   
# 2. OUTPUT:
#     
#     * a set of all the primes $p$ satisfying `a` $\leq p \leq$ `b`
#     
# EXAMPLE:
# 
# `>> primes(1, 10)`
# 
# `{2, 3, 5, 7}`
# 
# `>> primes(50, 100)`
# 
# `{53, 59, 61, 67, 71, 73, 79, 83, 89, 97}`
# 
# Note: the order of the elements might be different in your output, and that is okay! As long as you have all the primes.
 
# In[6]:
 
 
import math
def primes(a, b):
    
    # Error checking
    if a < 1:
        raise ValueError
    if b < a:
        raise ValueError
        
    # Adding all numbers a to b 
    list_a_b = []  
    for i in range (a, b + 1):
        list_a_b.append(i)
       
    for j in range(2, math.ceil(math.sqrt(b)) + 1):  # From 2 to the square root of b 
        composite = []
        for k in range(len(list_a_b)):
            if (list_a_b[k] % j == 0 and list_a_b[k] != j) or (list_a_b[k] == 1): # Checks to see if value is composite or 1
                if list_a_b[k] not in composite: # If composite value / 1 is not in the list
                    composite.append(list_a_b[k]) # Value gets appended
                    
        list_a_b = list(set(list_a_b) - set(composite))
            
    return set(list_a_b)
 
 
# ----------------------------------------------
# 
# #### Problem 2:
# 
# Create a function `bezout_coeffs(a, b)` that computes the Bezout coefficients `s` and `t` of `a` and `b`.
# 
# 1. INPUT: 
#     * `a`,`b` - distinct integers
# 
# 2. OUTPUT: `{a: s, b: t}` - dictionary where keys are the input integers and values are their corresponding Bezout coefficients.
# 
# EXAMPLE:  
#  
# `>> bezout_coeffs(414, 662)` 
# 
# `{414 : 8, 662 : -5}`
# 
# 
 
# #### HINT:
# 
# 
# To come up with an algorithm for the function `bezout_coeff(a,b)` consider the following example:
# 
# Suppose $a = 13,\;\; b = 21$.  We seek $s$ and $t$ such that gcd$(13, 21) = 13s + 21t$
# 
# Let's begin by defining $s_0 = 1, \;\; t_0 = 0, \;\; a_1 = 13,\;\; b_1 = 21$.  At every round in attempting to attain the gcd, we will refer to $s_i$ and $t_i$ as the current coefficients of 13 and 21, respectively.
# 
# 
# **Round 1:**
# 
# $21 = 1 \cdot 13 +8  $
# 
# $\hspace{2cm} \implies 8 = 21 - 1 \cdot 13$  We will call this EQN 1
# 
# $\hspace{2cm} \implies s_1 = -1, \hspace{0.5cm} t_1 = 1$
# 
# NOTICE:
# 
# $\hspace{2cm} s_1 = - \; ( \; b_1 \textbf{ div } a_1 \; ) = -(21 \textbf{ div } 13) = -1 $
# 
# 
# 
# **Round 2:**
# 
# $a_2 = 8,\;\; b_2 = 13$
# 
# $13 = 1 \cdot 8 + 5 $
# 
# $\hspace{2cm} \implies 5 = 13 - 1 \cdot 8$
# 
# $\hspace{3.5cm} = 1 \cdot 13 - 1 (21 - 1 \cdot 13) $  from EQN 1
# 
# $\hspace{3.5cm} = 2 \cdot 13 - 1 \cdot 21 $
# 
# $\hspace{2cm} \implies s_2 = 2, \hspace{0.5cm} t_2 = -1$
# 
# 
# NOTICE:
# 
# $\hspace{2cm} s_2 = s_0 -  s_1\; (\; b_2\textbf{ div }a_2 ) $
# 
# $\hspace{2.5cm} = 1 -  1\; (\; 13\textbf{ div }8) $
# 
# $\hspace{2.5cm} = 1 -\;( -1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\hspace{2cm} t_2 = t_0 - t_1\; (\; b_2\textbf{ div }a_2 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (\; 13\textbf{ div }8 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (1)$
# 
# $\hspace{2.5cm} = -1$
# 
# 
# **Round 3:**
# 
# $a_3 = 5,\;\; b_3 = 8$
# 
# $8 = 1 \cdot 5 + 3$
# 
# $\hspace{2cm} \implies 3 = 8 - \underbrace{1}_{b_3\textbf{ div }a_3} \cdot 5$
# 
# $\hspace{3.5cm} = 1 \cdot (\underbrace{1}_{t_1}  \cdot 21 \underbrace{-1}_{s_1}  \cdot 13) - \underbrace{1}_{b_3\textbf{ div }a_3} (\underbrace{2}_{s_2}  \cdot 13 \underbrace{-1}_{t_2}  \cdot 21 ) $
# 
# $\hspace{3.5cm} = - 3 \cdot 13 + 2 \cdot 21$
# 
# $\hspace{2cm} \implies s_3 = -3, \hspace{0.5cm} t_3 = 2$
# 
# 
# 
# NOTICE:
# 
# $\hspace{2cm} s_3 = s_1 -s_2 \; ( \; b_3\textbf{ div }a_3) $
# 
# $\hspace{2.5cm} = -1 -(2)(1) $
# 
# $\hspace{2.5cm} = -3$
# 
# $\hspace{2cm} t_3 = t_1 - t_2 \; ( \; b_3\textbf{ div }a_3)$
# 
# $\hspace{2.5cm} = 1 -(-1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\vdots$
# 
# **Round $k$:**
# 
# For any round $k \geq 2$, the corresponding $s_k$ and $t_k$ values are given by
# 
# * $s_k = s_{k-2} - s_{k-1} \;(\; b_{k} \textbf{ div } a_{k})$
# 
# * $t_k = t_{k-2} - t_{k-1} \; (\; b_{k} \textbf{ div } a_{k})$
# 
# 
# 
# You should verify for yourself that for any $a, b$,
# * $s_0 = 1$
# * $t_0 = 0$
# * $s_1 = -(\; b \textbf{ div } a)$
# * $t_1 = 1$
# 
# 
# 
 
# In[52]:
 
 
def bezout_coeffs(a, b):
    
    # str to int
    int(a)
    int(b)
    
    s = [1, (-(b // a))]
    t = [0, 1]
    
    loc = 2 # k, keep track of index
    a_list = [a]
    b_list = [b]
    
    # While a or b can't be divided by number that is calculated with the current numbers (the ones that are stored in the
    # process of getting Bezout coefficients)
    while True:
 
        if ((s[len(s) - 1] * a) + (t[len(t) - 1] * b)) == 0 or ((s[len(s) - 1] * a) + (t[len(t) - 1] * b)) == 0:
            break
            
        if (a % ((s[len(s) - 1] * a) + (t[len(t) - 1] * b))) == 0 and (b % ((s[len(s) - 1] * a) + (t[len(t) - 1] * b))) == 0:
            break
        
        a_list.append(b_list[len(b_list) - 1] % a_list[len(a_list) - 1])
        b_list.append(a_list[len(a_list) - 2])
 
        s.append(s[loc - 2] - s[loc - 1] * (b_list[loc - 1] // a_list[loc - 1]))
        t.append(t[loc - 2] - t[loc - 1] * (b_list[loc - 1] // a_list[loc - 1]))
        
        loc += 1
        
    return {a: s[len(s) - 1], b: t[len(t) - 1]}
 
 
# ----------------------------------------------------------------------
# #### Problem 3:
# 
# Create a function `gcd(a, b)` that computes the greatest common divisor of `a` and `b` using the `bezout_coeff` function you implemented for problem 2 lecture.  No credit will be given to functions that employ any other implementation.  For example, using the built-in function `math.gcd()` as part of our implementation will not receive any credit.
# 
# 1. INPUT: 
#     * `a`,`b` - integers
# 
# 2. OUTPUT: `d` - the gcd
# 
# EXAMPLE:  
#  
# `>> gcd(414, 662)` 
# 
# `2`
 
# #### HINT
# 
# The GCD of any two numbers must be positive by definition.
 
# In[53]:
 
 
def gcd(a, b):
    
    int(a)
    int(b)
    
    if a == 0 or b == 0:
        return max(a, b)
    
    gcd = bezout_coeffs(a, b)
    num = list(gcd.keys())
    coeffs = list(gcd.values())
    
    return abs((num[0] * coeffs[0]) + (num[1] * coeffs[1]))