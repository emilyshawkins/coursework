#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229 Final Exam Part 1: Take Home
# 
# #### Due Date: 
# 
# Tuesday, 5/9 @ 11:59 PM
# 
# #### Worth:
# 
# 15% of the Final Exam grade category
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit **to CodePost** by the due date this file converted to a Python script named `final.py`.
# 
# ----------------------------------------------------------
# 
# #### Background:
# 
# In this programming assignment, you will be responsible for implementing a solver for the system of linear equations $A \overrightarrow{x} = \overrightarrow{b}$ where 
# 
# * $A$ is an $n \times n$ matrix whose columns are linearly independent
# * $\overrightarrow{x} \in \mathbb{R}^n$
# * $\overrightarrow{b} \in \mathbb{R}^n$
# 
# To implement the solver, you must apply the following theorem:
# 
# **THM |  QR-Factorization** 
# 
# If $A \in \mathbb{F}_{m \times n}$ matrix with linearly independent columns $\overrightarrow{a_1}, \overrightarrow{a_2}, \dots \overrightarrow{a_n}$, then there exists,
# 
# 1. an $m \times n$ matrix $Q$ whose columns $\overrightarrow{u_1}, \overrightarrow{u_2}, \dots, \overrightarrow{u_n}$ are orthonormal, and 
# 2. an $n \times n$ matrix $R$ that is upper triangular and whose entries are defined by,
# $r_{ij} = \begin{cases}
# \langle \overrightarrow{u_i}, \overrightarrow{a_j} \rangle & \text{ for } i \leq j \\
# 0 & \text{ for } i > j \\
# \end{cases}$
# 
# such that $A = QR$.  This referred to as the QR factorization (or decomposition) of matrix $A$.
# 
# 
# To find matrices $Q$ and $R$ from the QR Factorization Theorem, we apply Gram-Schimdt process to the columns of $A$.  Then,
# 
# * the columns of $Q$ will be the orthonormal vectors $\overrightarrow{u_1}, \overrightarrow{u_2}, \dots, \overrightarrow{u_n}$ returned by the Gram Schimdt process, and
# * the entries $r_{ij}$ of $R$ will be computed using each column $\overrightarrow{u_i}$ as defined in the theorem.
# 
 
# -----------------------------------------------------
# 
# #### Your Task:
# 
# Assuming $A \in \mathbb{R}_{n \times n}$ is a `Matrix` object, and $\overrightarrow{b} \in \mathbb{R}^n$ is a `Vec` object, implement a function `solve_QR(A, b)` that uses the QR-factorization of $A$ to compute and return the solution to the system $A\overrightarrow{x} =  \overrightarrow{b}$.  The returned object should be of type `Vec`.  You must use your function, `gram_schimdt(S)` from `pa6.py` to implement `solve_QR()`.  You may NOT use any other Python library or built-in functions that already perform part or the entire algorithm.  
# 
# HINT:  If $A = QR$, then $A\overrightarrow{x} = \overrightarrow{b}$ becomes $QR\overrightarrow{x} = \overrightarrow{b}$.  What happens if we multiply both sides of the equation by the transpose of $Q$? i.e., What does $Q^tQR\overrightarrow{x} = Q^t\overrightarrow{b}$ simplify to?
 
# In[20]:
 
 
import pa6
from random import randint
 
 
# In[21]:
 
 
def solve_QR(A, b):
    
    vectors = []
    for i in range(len(A.colsp)):
        vectors.append(pa6.Vec(A.colsp[i]))
    
    ortho_col = pa6.gram_schmidt(vectors) # gram_schmidt for vectors
    
    Q_2d = [] # To get Q
    for j in range(len(ortho_col[0].elements)): 
        row = []
        for k in range(len(ortho_col)):
            row.append(ortho_col[k].elements[j])
        Q_2d.append(row)
        
    Q_t_2d = [] # To get Q transposed
    for a in range(len(ortho_col)):
        row = []
        for c in range(len(ortho_col[0].elements)):
            row.append(ortho_col[a].elements[c])
        Q_t_2d.append(row)
        
    R_2d = [] # To get R
    for x in range(len(ortho_col)):
        row = []
        for y in range(len(ortho_col)):
            if x <= y:
                row.append(pa6.Vec(Q_t_2d[x]) * pa6.Vec(A.colsp[y]))
            if x > y:
                row.append(0)
        R_2d.append(row)
        
    Q_mat = pa6.Matrix(Q_2d)
    Q_t_mat = pa6.Matrix(Q_t_2d)
    R_mat = pa6.Matrix(R_2d)
    
    product = Q_t_mat * b # The product of Q transposed and Vector b
    
    for d in range(len(R_2d)): # Augmented R
        R_2d[d].append(product.elements[d])
        
    calc = [0] * len(R_2d) # Number of rows, R is a square matrix
        
    last = 1
 
    for e in range(len(R_2d) - 1, -1, -1): # Checks for rows with all zeros
        if R_2d[e] == [0] * len(R_2d):
            last += 1
 
    last_var = R_2d[len(R_2d) - last][len(R_2d[0]) - 1] # Answer to the last expression in the matrix
    single_var = R_2d[len(R_2d) - last][len(R_2d[0]) - 2] # Number in the last expression in the matrix
    
    calc[len(R_2d) - last] = last_var / single_var # Entry for lowest non-zero row
 
    flag = len(R_2d[0]) - 2
 
    for f in range(len(R_2d) - last -1, -1, -1): # Every row from the bottom (-1)
        
        calc_to = R_2d[f][len(R_2d[0]) - 1] # Last row element
        
        for g in range(len(R_2d[0]) - 2, flag - 1, -1):                
 
            calc_to -= R_2d[f][g] * calc[g]
            
        flag -= 1
        calc_to /= R_2d[f][g - 1]
        calc[f] = calc_to
 
    for z in range(len(calc) - 1, -1, -1):
        if calc[z] == 0:
            calc.pop()
        else:
            calc[z] = round(calc[z])
 
 
    return pa6.Vec(calc)
 
 
# In[22]:
 
 
# """TESTER CELL"""
# n = randint(3, 5)
 
# rowsp = [[randint(-30, 30) for i in range(n)] for j in range(n)]
 
# while not pa6.is_independent([pa6.Vec(row) for row in rowsp]):
#     rowsp = [[randint(-30, 30) for i in range(n)] for j in range(n)]
 
# A = pa6.Matrix(rowsp)
# x_true = pa6.Vec([randint(-10, 10) for i in range(n)])
 
# b = A * x_true
# print("Expected:", x_true)
 
# x = solve_QR(A, b)
# print("Returned:", x)
 