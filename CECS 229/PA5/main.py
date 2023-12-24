#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229 Programming Assignment #5
# 
# #### Due Date: 
# 
# Sunday, 4/9 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the to CodePost a file named `pa5.py` by the due date:
# 
# 
# #### Objectives:
# 
# 1. Define a matrix data structure with relevant matrix operations.
# 2. Understand the role of matrices in simple image processing applications. 
# 
# 
# 
 
# --------------------------------------------------------
# 
# #### Problem 1.
# 
# 
# Implement a class `Matrix` that creates matrix objects with attributes
# 1. `colsp` -column space of the `Matrix` object, as a list of columns (also lists)
# 2. `rowsp` -row space of the `Matrix` object, as a list of rows (also lists)
# 
# The constructor takes a list of rows as an argument, and constructs the column space from this rowspace.  If a list is not provided, the parameter defaults to an empty list.
# 
# You must implement the following methods in the `Matrix` class:
# 
# ***Setters***
# * `set_col(self, j, u)` - changes the j-th column to be the list `u`.  If `u` is not the same length as the existing columns, then the method raises a `ValueError` with the message `Incompatible column length.`
# * `set_row(self,i, v)` - changes the i-th row to be the list `v`.  If `v` is not the same length as the existing rows, then method raises a `ValueError` with the message `Incompatible row length.`
# * `set_entry(self,i, j, x)` - changes the existing $a_{ij}$ entry in the matrix to `x`.
# 
# ***Getters***
# * `get_col(self, j)` - returns the j-th column as a list.  
# * `get_row(self, i)` - returns the i-th row as a list `v`. 
# * `get_entry(self, i, j)` - returns the existing $a_{ij}$ entry in the matrix.
# * `col_space(self)` - returns the *list* of vectors that make up the column space of the matrix object
# * `row_space(self)` - returns the *list* of vectors that make up the row space of the matrix object
# * `get_diag(self, k)` - returns the $k$-th diagonal of a matrix where $k =0$ returns the main diagonal,
# $k > 0$ returns the diagonal beginning at $a_{1(k+1)}$, and $k < 0$ returns the diagonal beginning at $a_{(-k+1)1}$.  e.g. `get_diag(1)` for an $n \times n$ matrix returns [$a_{12}, a_{23}, a_{34}, \dots, a_{(n-1)n}$]
# * `__str__(self)` - returns a formatted string representing the matrix entries as 
# 
# $\hspace{10cm} \begin{array} aa_{11} & a_{12} & \dots & a_{1m} \\ a_{21} & a_{22} & \dots & a_{2m} \\ \vdots & \vdots & \ddots & \vdots \\a_{m1} & a_{m2} & \dots & a_{mn} \end{array}$
# 
# ***Overloaded operators***
# 
# In addition to the methods above, the `Matrix` class must also overload the `+`, `-`, and `*` operators to support:
# 
# 1. `Matrix + Matrix` addition
# 2. `Matrix - Matrix` subtraction
# 3. `Matrix * scalar` multiplication
# 4. `Matrix * Matrix` multiplication
# 5. `Matrix * Vec` multiplication
# 6. `scalar * Matrix` multiplication
 
# In[13]:
 
 
"REPLACE THE BOTTOM WITH YOUR Matrix CLASS "
 
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
 