#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229 Programming Assignment #6
# 
# #### Due Date: 
# 
# Sunday, 4/30 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost a Python script named `pa6.py` with your work by the due date.
# 
# #### Objectives:
# 
# 1. Apply Gaussian Elimination to solve the system $A \overrightarrow{x} = \overrightarrow{b}$.
# 2. Use Lp -norm to calculate the error in a solution given by applying Gaussian elimination.
# 3. Use the REF of the augmented matrix for the system $A \overrightarrow{x} = \overrightarrow{b}$ to determine if it has one solution, no solution, or infinitely-many solutions.
# 4. Determine the number of free variables that the system $A \overrightarrow{x} = \overrightarrow{b}$ has if it has infinitely-many solutions.
# 5. Determine whether a set of column-vectors is linearly dependent by forming and solving a system of the form $A \overrightarrow{x} = \overrightarrow{0}$.
# -----------------------------------------
# 
# 
 
# #### Problem 1
# 
# Copy-paste your implemented `Matrix` and `Vec` classes to the next cell.  Then, complete the following tasks:
# 
# 1. Add a method `norm(self, p)` to your `Vec` class so that if `u` is a `Vec` object, then `u.norm(p)` returns the $L_p$-norm of vector `u`.  Recall that the $L_p$-norm of an $n$-dimensional vector $\overrightarrow{u}$ is given by, $||u||_p = \left( \sum_{i = 1}^{n} |u_i|^p\right)^{1/p}$.  Input `p` should be of the type `int`.  The output norm should be of the type `float`.
# 2. Add a method `ref(self)` that applies Gaussian Elimination to create and return the Row Echelon Form of the current matrix.  The output must be of the type `Matrix`.  The method should ***NOT*** modify the contents of `self.rowsp` or `self.colsp`.  It should create and return a new `Matrix` object.
# 3. Add a method `rank(self)` to your `Matrix` class so that if `A` is a `Matrix` object, then `A.rank()` returns the rank of `A`.
 
# In[181]:
 
 
class Vec:
    def __init__(self, contents = []):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
    
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        inner_total = 0
        
        for i in self.elements:
            inner_total += i ** 2
            
        return math.sqrt(inner_total)
        
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
            
        vector_sum = []
        
        for i in range(len(self.elements)):
            vector_sum.append(self.elements[i] + other.elements[i])
        
        return Vec(vector_sum)
    
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
            
        vector_difference = []
        
        for i in range(len(self.elements)):
            vector_difference.append(self.elements[i] - other.elements[i])
        
        return Vec(vector_difference)
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            if len(self.elements) != len(other.elements):
                raise ValueError()
            
            vector_dot = 0
        
            for i in range(len(self.elements)):
                vector_dot += self.elements[i] * other.elements[i]
        
            return vector_dot
            
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            vector_product = []
            
            for i in range(len(self.elements)):
                vector_product.append(self.elements[i] * other)
                
            return Vec(vector_product)
            
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        if type(other) == float or type(other) == int: #scalar-vector multiplication
            vector_product = []
            
            for i in range(len(self.elements)):
                vector_product.append(self.elements[i] * other)
                
            return Vec(vector_product)
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return f'{self.elements}' # does NOT need further implementation
    
    def __repr__(self):
        return f'{self.elements}'
    
    def norm(self, p):
        
        inter_sum = 0
        
        for i in range(len(self.elements)):
            inter_sum += abs(self.elements[i]) ** p
            
        return inter_sum ** (1 / p)
 
 
class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)
        
    def _construct_cols(self, rowsp):
        colsp = []
        
        for i in range(len(rowsp[0])):
            col = []
            for j in range(len(rowsp)):
                col.append(rowsp[j][i])
            colsp.append(col)
        
        return colsp
           
    def __add__(self, other):
        if len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp):
            matrix_sum = []
            for i in range(len(self.rowsp)):
                row_list = []
                for j in range(len(self.colsp)):
                    row_list.append(self.rowsp[i][j] + other.rowsp[i][j])
                matrix_sum.append(row_list)
            return Matrix(matrix_sum)
        else:
            raise ValueError
    
    def __sub__(self, other):
        if len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp):
            matrix_diff = []
            for i in range(len(self.rowsp)):
                row_list = []
                for j in range(len(self.colsp)):
                    row_list.append(self.rowsp[i][j] - other.rowsp[i][j])
                matrix_diff.append(row_list)
            return Matrix(matrix_diff)
        else:
            raise ValueError
        
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            scalar_prod = []
            for i in range(len(self.rowsp)):
                row_list = []
                for j in range(len(self.colsp)):
                    row_list.append(other * self.rowsp[i][j])
                scalar_prod.append(row_list)
            return Matrix(scalar_prod)
                
        elif type(other) == Matrix:
            if len(self.colsp) == len(other.rowsp):
                matrix_prod = []
                for i in range(len(self.rowsp)):
                    row_list = []
                    for j in range(len(other.colsp)):
                        temp_sum = 0
                        for k in range(len(self.colsp)):
                            temp_sum += self.rowsp[i][k] * other.colsp[j][k]
                        row_list.append(temp_sum)
                    matrix_prod.append(row_list)
                return Matrix(matrix_prod)
            else:
                raise ValueError
            
        elif type(other) == Vec:
            if len(self.colsp) == len(other.elements):
                matrix_vec = []
                for i in range(len(self.rowsp)):
                    row_list = []
                    for j in range(1):
                        temp_sum = 0
                        for k in range(len(self.colsp)):
                            temp_sum += self.rowsp[i][k] * other.elements[k]
                        row_list.append(temp_sum)
                    matrix_vec.append(row_list)
                matrix_vec_prod = []
                for m in range(len(matrix_vec)):
                    matrix_vec_prod.append(matrix_vec[m][0])
                return Vec(matrix_vec_prod)
            return
            
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float or type(other) == int:
            scalar_prod = []
            for i in range(len(self.rowsp)):
                row_list = []
                for j in range(len(self.colsp)):
                    row_list.append(other * self.rowsp[i][j])
                scalar_prod.append(row_list)
            return Matrix(scalar_prod)
        
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rowsp:
            mat_str += f'{row}' + "\n"
        return f'{mat_str}'
                
    def __eq__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()
 
    def __req__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()
    
    
    
    
    
    def set_col(self, j, u):
        """Changes the j-th column to be the list u. If u is not the same length as the
        existing columns, a ValueError is raised with the message Incompatible column length"""
        
        if len(u) != len(self.rowsp):
            raise ValueError('Incompatible column length')
        
        for i in range(len(u)):
            self.rowsp[i][j - 1] = u[i]
            
        self.colsp = self._construct_cols(self.rowsp)
        
    def set_row(self, i, v):
        """Changes the i-th row to be the list v. If v is not the same length as the
        existing rows, then method raises a ValueError with the message Incompatible row length"""
        
        if len(v) != len(self.colsp):
            raise ValueError('Incompatible row length')
        
        self.rowsp[i - 1] = v
        self.colsp = self._construct_cols(self.rowsp)
        
    def set_entry(self, i, j, x):
        """Changes the existing a[i][j] entry in the matrix to x"""
 
        self.rowsp[i - 1][j - 1] = x
        self.colsp = self._construct_cols(self.rowsp)
        
    def get_col(self, j):
        """Returns the j-th column as a list"""
        
        return self.colsp[j - 1]
        
    def get_row(self, i):
        """Returns the i-th row as a list"""
        
        return self.rowsp[i - 1]
        
    def get_entry(self, i, j):
        """Returns the existing a[i][j] entry in the matrix"""
        
        return self.rowsp[i - 1][j - 1]
        
    def col_space(self):
        """Returns the list of vectors that make up the column space of the matrix object"""
        
#         colspace = []
#         for i in self.colsp:
#             colspace.append(Vec(i))
            
#         return colspace
 
        return self.colsp
        
    def row_space(self):
        """Returns the list of vectors that make up the row space of the matrix object"""
        
#         rowspace = []
#         for i in self.rowsp:
#             rowspace.append(Vec(i))
#         return rowspace
        
        return self.rowsp
 
    
    
    
    
    def get_diag(self, k):
        """Returns the k-th diagonal of a matrix where k = 0 returns the main diagonal, k > 0 returns the 
        diagonal beginning at a[1][k + 1], and k < 0 returns the diagonal beginning at a[-k + 1][1]"""
        
        diagonal = []
        
        if k == 0:
            for i in range(min(len(self.rowsp), len(self.colsp))):
                diagonal.append(self.rowsp[i][i])
            return diagonal
        elif k < 0:
            for i in range(min(len(self.rowsp), len(self.colsp)) + k):
                diagonal.append(self.rowsp[i - k][i])
            return diagonal
        elif k > 0:
            for i in range(min(len(self.rowsp), len(self.colsp)) - k):
                diagonal.append(self.rowsp[i][i + k])
            return diagonal
        
    def ref(self):
        
        ref_mat = []
        for a in range(len(self.rowsp)): # Dup original matrix
            row = []
            for b in range(len(self.colsp)):
                row.append(self.rowsp[a][b])
            ref_mat.append(row)
            
        for j in range(len(ref_mat) - 1): # Pivots, rows
            
            pivot = 0
            
            temp_len = []
 
            for d in range(len(ref_mat)): # Swapping
                len_tup = ()
                for e in range(len(ref_mat[0])):
                    if ref_mat[d][e] != 0:
                        len_tup += (e,)
                        len_tup += (d,)
                        break
                if ref_mat[d] == [0] * len(ref_mat[d]):
                    len_tup += (len(ref_mat[d]), d)
                temp_len.append(len_tup)
            temp_len.sort()
 
            temp_ref = [0] * len(ref_mat)
            for f in range(len(ref_mat)):
                temp_ref[f] = ref_mat[temp_len[f][1]]
 
            ref_mat = temp_ref
 
            
            for i in range(j + 1, len(ref_mat)): # Rows to calculate
                
                ref_col = 0
                for c in range(len(ref_mat[0])):
                    if ref_mat[j][c] != 0:
                        pivot = ref_mat[j][c]
                        ref_col = c
                        break
                        
                if pivot == 0:
                    break
 
                ref_mat[i] = (Vec(ref_mat[i]) - ((ref_mat[i][c] / pivot) * Vec(ref_mat[j]))).elements
                
                for h in range(len(ref_mat[i])): # Rounding
                    
                    ref_mat[i][h] = round(ref_mat[i][h], 5)
 
            if pivot == 0:
                break
                    
        for x in range(len(ref_mat)): # Rounding
            for y in range(len(ref_mat[0])):
                ref_mat[x][y] = round(ref_mat[x][y], 1)
                
        #print(self)
        #print(Matrix(ref_mat))
        return Matrix(ref_mat)
    
    def rank(self):
        ref_mat = self.ref()
        rank = 0
 
        for i in range(len(ref_mat.rowsp)):
            if ref_mat.rowsp[i] != [0] * len(ref_mat.rowsp[i]):
                rank += 1
        
        return rank
 
 
# #### Problem 2
# 
# Implement the function `gauss_solve(A, b)` that solves the system $A \overrightarrow{x} = \overrightarrow{b}$.  The input `A` is of the type `Matrix` and `b` is of the type `Vec`.
#    - If the system has a unique solution, it returns the solution as a `Vec` object.  
#    - If the system has no solution, it returns `None`. 
#    - If the system has infinitely many solutions, it returns the number of free variables (`int`) in the solution.
 
# In[229]:
 
 
def gauss_solve(A, b):
    
    aug_mat = []
    
    for k in range(len(A.rowsp)): # Initialize augmented matrix
        row = []
        for d in range(len(A.colsp) + 1):
            row.append(0)
        aug_mat.append(row)
    aug_mat = Matrix(aug_mat)
 
    for i in range(1, len(aug_mat.rowsp) + 1): # Fill
        for j in range(1, len(aug_mat.colsp)):
            entry = A.get_entry(i, j)
            aug_mat.set_entry(i, j, entry)
            if j == len(aug_mat.colsp) - 1:
                aug_mat.set_entry(i, j + 1, b.elements[i - 1])
 
    if A.rank() < aug_mat.rank():
        return None
    
    if A.rank() == aug_mat.rank() and A.rank() < len(A.colsp):
        free = -1
        for s in range(len(aug_mat.ref().colsp) - 1):
            if aug_mat.ref().rowsp[aug_mat.ref().rank() - 1][s] != 0:
                free += 1
        return free
                       
    if A.rank() == aug_mat.rank() == len(A.colsp):
        ag_ref = aug_mat.ref()
        print(ag_ref)
        calc = [0] * len(ag_ref.rowsp)
        
        last = 1
        
        for i in range(len(ag_ref.rowsp) - 1, -1, -1):
            if ag_ref.rowsp[i] == [0] * len(ag_ref.colsp):
                last += 1
                
        last_eq = ag_ref.get_entry(len(ag_ref.rowsp) - last + 1, len(ag_ref.colsp))
        single = ag_ref.get_entry(len(ag_ref.rowsp) - last + 1, len(ag_ref.colsp) - 1)
        calc[len(ag_ref.rowsp) - last] = (last_eq / single)
        
        flag = len(ag_ref.colsp) - 2
        last_ent = 0
        
        for g in range(len(ag_ref.rowsp) - last, 0, -1): # Every row from the bottom (-1)
            calc_to = ag_ref.get_entry(g, len(ag_ref.colsp))
 
            for h in range(len(ag_ref.colsp) - 1, flag, -1):
                
                
                print(ag_ref.get_entry(g, h), calc[h - 1])
                
                calc_to -= ag_ref.get_entry(g, h) * calc[h - 1]
                
            
            flag -= 1
            calc_to /= ag_ref.get_entry(g, h - 1)
            calc[g - 1] = calc_to
            
        for z in range(len(calc) - 1, -1, -1):
            if calc[z] == 0:
                calc.pop()
            else:
                calc[z] = round(calc[z])
            
            
        return Vec(calc)
 
# a = Matrix([[-6, 13, -12, -12, -15, 9, -3],
# [10, -4, 9, -7, 11, 13, 6],
# [-18, 1, 9, -16, 1, -17, -3],
# [-18, -10, -12, -10, 11, 19, -20],
# [3, 20, -15, -3, 3, 11, -13],
# [-2, 14, -11, 12, 8, -9, -1],
# [7, -19, 13, -2, 13, 20, -18],
# [-7, -14, -11, 18, 0, 14, 0],
# [-17, -12, -3, -8, -16, -16, -6]])
 
# b = Vec([122, 84, -117, 409, 445, 158, 191, 6, -244])
 
# print(gauss_solve(a, b))
 
 
# 
# ------------------------------------------------
# 
# #### Problem 3
# 
# Implement the function `is_independent(S)` that returns `True` if the set `S` of `Vec` objects is linearly **independent**, otherwise returns `False`.
 
# In[48]:
 
 
def is_independent(S):
    
    testing = []
    for i in range(len(S[0].elements)):
        row = []
        for k in range(len(S)):
            row.append(S[k].elements[i])
        testing.append(row)
        
    equals = []
    for j in range(len(S[0].elements)):
        equals.append(0)
 
    result = gauss_solve(Matrix(testing), Vec(equals))
    if type(result) == int:
        return False
    return True
    
 
 
# #### Problem 4
# 
# Implement the function `gram_schmidt(S)` that applies the Gram-Schmidt process to create an orthonormal set of vectors from the vectors in `S`.  The function raises a `ValueError` if the set `S` is NOT linearly independent.
# 
# INPUT:
#  - `S` a set of `Vec` objects
# 
# OUTPUT:
#  - a set of `Vec` objects representing orthonormal vectors.
#  
# HINT:  
# 
# If $S = \{\overrightarrow{x_1}, \overrightarrow{x_2}, \dots ,\overrightarrow{x_n}\}$ is a set of linearly independent vectors, then Gram-Schmidt process returns the set $\{\overrightarrow{u_1}, \overrightarrow{u_2}, \dots ,\overrightarrow{u_n}\}$
# where,
# - $\overrightarrow{u_i} = \frac{1}{||\overrightarrow{w_i}||_2}\overrightarrow{w_i} \hspace{1cm}$ for $i = 1, 2, \dots n$, 
# 
# and
# 
# - $\overrightarrow{w_1} = \overrightarrow{x_1}$
# - $\overrightarrow{w_i} = \overrightarrow{x_i} - \sum_{j = 1}^{i-1} proj_{\overrightarrow{w_j}}(\overrightarrow{x_i}) \hspace{1cm} $ for $i = 2, 3, \dots n$ 
 
# In[50]:
 
 
def gram_schmidt(S):
    
    if not is_independent(S):
        raise ValueError
 
    w_list = []
    w_list.append(S[0])
 
    for i in range(1, len(S)):
        temp_comp = S[i]
        for j in range(i):
            temp_comp -= ((w_list[j] * S[i]) / (w_list[j] * w_list[j])) * w_list[j]
        w_list.append(temp_comp)
 
    ortho = []
    for k in range(len(w_list)):
        denom = w_list[k].norm(2)
        vec = []
        for a in range(len(w_list[k].elements)):
            vec.append(float(f'{(w_list[k].elements[a] / denom):.6f}'))
 
        ortho.append(Vec(vec))
 
    return ortho
 