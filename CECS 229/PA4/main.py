#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229 Programming Assignment #4
# 
# #### Due Date: 
# 
# Sunday, 3/19 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment, you must submit to CodePost this file converted to a Python script named `pa4.py`
# 
# #### Objectives:
# 
# 1. Apply vector operations to translate, scale, and rotate a set of points representing an image.
# 2. Perform various operations with or on vectors: addition, subtraction, dot product, norm.
# 
# 
# --------------------------------------------------------
# 
# #### Needed Import Statements
 
# In[3]:
 
 
# MAKE SURE TO RUN THIS CELL BEFORE RUNNING ANY TESTER CELLS
"""
In order for the import statements below to work, you must download and save 
the plotting.py and image.py files to the same folder where this file is located.
""" 
import math
from plotting import plot
import image
 
 
# #### Problem 1:
# 
# Create a function `translate(S, z0)` that translates the points in the input set $S$ by $z_0 = a_0 + b_0 i$.  The function should satisfy the following:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `z0` - complex number
# 2. OUTPUT:
#     * a set consisting of points in S translated by $z_0$
 
# In[4]:
 
 
def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * a set consisting of points in S translated by z0
    """
    
    translated = set()
    
    for i in S:
        real = i.real + z0.real
        imaginary = i.imag + z0.imag
        translated.add(complex(real, imaginary))
        
    return translated
 
 
# In[5]:
 
 
# """
# TESTER CELL #1 FOR translate()
# """
 
# S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
 
 
# print("ORGINAL VALUES:", S)
 
# plot([(S, 'black')], 10, title = "Original Values") # original values will be plotted in black
 
# T1 = translate(S, -3-2j)  # values translated by -3-2i will be plotted in red
# T2 = translate(S, 3-2j)   # values translated by 3-2i will be plotted in green
# T3 = translate(S, -3+2j)  # values translated by -3+2i will be plotted in orange
# T4 = translate(S, 3+2j)   # values translated by 3+2i will be plotted in blue
 
# print("SHIFT LEFT 3, DOWN 2:", T1)
# print("Expected: {0j, (-0.25-1j), (-1+0j), -1j, (-1-1j), (-1.25-1j), (-0.75-1j), (0.25-1j), (-0.5-1j)}\n")
# print("\nSHIFT RIGHT 3, DOWN 2:", T2)
# print("Expected: {(6-1j), (6.25-1j), (5+0j), (6+0j), (5-1j), (5.75-1j), (5.5-1j), (4.75-1j), (5.25-1j)}\n")
# print("\nSHIFT LEFT 3, UP 2:", T3)
# print("Expected: {(-1+3j), (-1.25+3j), (-0.75+3j), (-1+4j), (-0.5+3j), 4j, (-0.25+3j), 3j, (0.25+3j)}\n")
# print("\nSHIFT RIGHT 3, UP 2:", T4)
# print("Expected: {(4.75+3j), (5.5+3j), (5.25+3j), (5+3j), (5+4j), (6+4j), (5.75+3j), (6+3j), (6.25+3j)}\n")
 
# # plotting original values against translated values
# plot([(S, 'black'), (T1, 'red'), (T2, 'green'), (T3, 'orange'), (T4, 'blue')], 10, title = "Original + Shifted Values")
 
 
# In[6]:
 
 
# """
# TESTER CELL #2 FOR translate()
# """
# img = image.file2image('img01.png')
# gray_img = image.color2gray(img)
# complex_img = image.gray2complex(gray_img)
# translated_img = translate(complex_img, -200 + 0j)
# plot([(complex_img, 'black')], 200, title = "Original Image")
# plot([(translated_img, 'black')], 200, title = "Translated Image")
 
 
# ------------
# 
# #### Problem 2:
# 
# Create a function `scale(S, k)` that scales the points in the input set $S$ by a factor of $k$:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `k` - positive float, raises ValueError if k $\leq$ 0.
# 2. OUTPUT:
#     * a set consisting of points in S scaled by $k$.
 
# In[7]:
 
 
def scale(S, k):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    
    scaled = set()
    
    for i in S:
        real = i.real * k
        imaginary = i.imag * k
        scaled.add(complex(real, imaginary))
        
    return scaled
    
 
 
# In[8]:
 
 
# """
# TESTER CELL #1 FOR scale()
# """
# sets = [S, T1, T2, T3, T4]
# scaled_sets = [scale(A, 2) for A in sets]
# for i in range(len(scaled_sets)):
#     print("Original Set:", sets[i])
#     print("After Scaling by 2:", scaled_sets[i], "\n")
 
# plot([(S, 'black')], 10, title = "Original Values")
# plot_data = list(zip(scaled_sets, ['black', 'red', 'green', 'orange', 'blue']))
# plot(plot_data, 10, title = "Scaled by 2") #second parameter affects window size
 
 
# In[9]:
 
 
# """
# TESTER CELL #2 FOR scale()
# """
# img = image.file2image('img01.png')
# gray_img = image.color2gray(img)
# complex_img = image.gray2complex(gray_img)
# scaled_img = scale(complex_img, 1.5)
# plot([(complex_img, 'black')], 200, title = "Original Image")
# plot([(scaled_img, 'black')], 200, title = "Image Scaled 1.5x")
 
 
# -----------------------------------
# 
# #### Problem 3:
# 
# Create a function `rotate(S, theta)` that rotates the points in the input set $S$ by $\theta$ radians:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `theta` - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
# 2. OUT:
#     * a set consisting of points in S rotated by $\theta$
 
# In[10]:
 
 
def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * a set consisting of points in S rotated by theta radians
        
    """
    
    rotated = set()
    
    for i in S:
        zmag = abs(math.sqrt((i.real ** 2) + (i.imag ** 2)))
        
        if i.real == 0 and i.imag == 0:
            rotated.add(complex(i.real, i.imag))
        elif i.real == 0 and i.imag > 0:
            angle = (math.pi / 2) + theta
            rotated.add(complex(zmag * math.cos(angle), zmag * math.sin(angle)))
        elif i.real == 0 and i.imag < 0:
            angle = -(math.pi / 2) + theta
            rotated.add(complex(zmag * math.cos(angle), zmag * math.sin(angle)))
        else:
            if i.real < 0:
                angle = math.atan(i.imag / i.real) + theta + math.pi
            else:
                angle = math.atan(i.imag / i.real) + theta
                
            rotated.add(complex(zmag * math.cos(angle), zmag * math.sin(angle)))
        
    return rotated
    
 
 
# In[11]:
 
 
# """
# TESTER CELL #1 FOR rotate()
# """
# rotated_sets = [rotate(A, math.pi/2) for A in sets]
# for i in range(len(rotated_sets)):
#     print("Original Set:", sets[i])
#     print("After Scaling by 2:", rotated_sets[i], "\n")
 
# plot_data_rot = list(zip(rotated_sets, ['black', 'red', 'green', 'orange', 'blue']))
# plot(plot_data_rot, 10, title = "Rotated by 90 degrees") #second parameter affects window size
 
# rotated_sets_2 = [rotate(A, -1*math.pi/2) for A in sets]
# for i in range(len(rotated_sets_2)):
#     print("Original Set:", sets[i])
#     print("After Scaling by 2:", rotated_sets_2[i], "\n")
    
 
# plot([(S, 'black'), (T1, 'red'), (T2, 'green'), (T3, 'orange'), (T4, 'blue')], 10, title = "Original Values")
 
# plot_data_rot_2 = list(zip(rotated_sets_2, ['black', 'red', 'green', 'orange', 'blue']))
# plot(plot_data_rot_2, 10, title = "Rotated by -90 degrees") #second parameter affects window size
 
 
# In[12]:
 
 
# """
# TESTER CELL #2 FOR rotate()
# """
# img = image.file2image('img01.png')
# gray_img = image.color2gray(img)
# complex_img = image.gray2complex(gray_img)
# rotated_img = rotate(complex_img, -1*math.pi/2)
# plot([(complex_img, 'black')], 200, title = "Original Image")
# plot([(rotated_img, 'black')], 200, title = "Image Rotated by -90 degrees")
 
 
# In[13]:
 
 
# """
# Full image transformation = rotation + scaling + translation
# """
# img = image.file2image('img01.png')
# gray_img = image.color2gray(img)
# complex_img = image.gray2complex(gray_img)
 
# rotated_img = rotate(complex_img, -1*math.pi/2)
# scaled_img = scale(rotated_img, 1.5)
# translated_img = translate(scaled_img, -125 + 150j)
 
# plot([(complex_img, 'black')], 200, title = "Original Image")
# plot([(translated_img, 'black')], 200, title = "Transformed Image")
 
 
# --------------------
# #### Problem 4:
# 
# Finish the implementation of class `Vec` which instantiates row-vector objects with defined operations of addition, subtraction, scalar multiplication, and dot product.  In addition, `Vec` class overloads the Python built-in function `abs()` so that when it is called on a `Vec` object, it returns the Euclidean norm of the vector.
# 
# 
# 
 
# In[14]:
 
 
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
        return str(self.elements) # does NOT need further implementation
 