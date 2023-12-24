#!/usr/bin/env python
# coding: utf-8
 
# # CECS 229 Programming Assignment #3
# 
# #### Due Date: 
# 
# Sunday, 3/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks:
 
# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.
 
# In[16]:
 
 
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
 
def gcd(a, b):
    
    int(a)
    int(b)
    
    gcd = bezout_coeffs(a, b)
    num = list(gcd.keys())
    coeffs = list(gcd.values())
    
    if a == 0 or b == 0:
        return max(a, b)
    
    if a == 1 or b == 1:
        return 1
    
    if a == b:
        return a
    
    return abs((num[0] * coeffs[0]) + (num[1] * coeffs[1]))
 
def modinv(a,m):
    """returns the smallest, positive inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: an integer in the range [0, m-1]
    """
    
    if gcd(a, m) != 1:   # Checks if gcd = 1
        raise ValueError('The given values are not relatively prime')
    
    a_bar = bezout_coeffs(a, m).get(a)   # Gets the coefficient of a
    
    if a_bar < 0 or a_bar > m - 1:   # Checks if a_bar is out of range
        a_bar = a_bar % m
    
    return a_bar
 
 
# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.
 
# In[22]:
 
 
def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    if gcd(a, 26) != 1:
        raise ValueError('The given key is invalid. The gcd(a,26) must be 1.')
        
    encrypted = ''
    text = letters2digits(text)
    
    for i in range(0, len(text), 2):
        c = (a * int(text[i: i + 2]) + b) % 26
        if len(str(c)) != 2:
            encrypted = encrypted + '0' + str(c)
        else:
            encrypted += str(c)
    
    return digits2letters(encrypted)
 
 
# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.
 
# In[27]:
 
 
def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    if gcd(a, 26) != 1:
        raise ValueError('The given key is invalid. The gcd(a,26) must be 1.')
    
    decrypted = ''
    ciphertext = letters2digits(ciphertext)
    for k in range(0, len(ciphertext), 2):
        p = (modinv(a, 26) * (int(ciphertext[k: k + 2]) - b)) % 26
        if len(str(p)) != 2:
            decrypted = decrypted + '0' + str(p)
        else:
            decrypted += str(p)
            
    return digits2letters(decrypted)
 
 
# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(message, n, e)` which encrypts a string `message` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.
 
# In[61]:
 
 
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
 
def encryptRSA(message, n, e):
    """encrypts the plaintext message, using RSA and the key (n = p * q, e)
    INPUT:  message - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """ 
    encrypted = ''
    message = letters2digits(message)
    
    if len(message) % blocksize(n) != 0:
        message = message + (letters2digits('X') * ((blocksize(n) - (len(message) % blocksize(n))) // 2)) 
        
    for i in range(0, len(message), blocksize(n)):
        c = mod_exp(int(message[i: i + blocksize(n)]), e, n)
        if len(str(c)) != blocksize(n):
            encrypted = encrypted + ('0' * (blocksize(n) - len(str(c)))) + str(c)
        else:
            encrypted += str(c)
            
    return encrypted
 
 
# In[63]:
 
 
# """--------------------- ENCRYPTION TESTER CELL ---------------------------"""
# encrypted1 = encryptRSA("STOP", 2537, 13)
# encrypted2 = encryptRSA("HELP", 2537, 13)
# encrypted3 = encryptRSA("STOPS", 2537, 13)
# print("Encrypted Message:", encrypted1)
# print("Expected: 2081 2182")
# print("Encrypted Message:", encrypted2)
# print("Expected: 0981 0461")
# print("Encrypted Message:", encrypted3)
# print("Expected: 2081 2182 1346")
 
 
# """--------------------- TEST 2 ---------------------------"""
# encrypted = encryptRSA("UPLOAD", 3233, 17)
# print("Encrypted Message:", encrypted)
# print("Expected: 2545 2757 1211")
 
 
# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.
 
# In[76]:
 
 
def decryptRSA(cipher, p, q, e):
    """decrypts cipher, which was encrypted using the key (p * q, e)
    INPUT:  cipher - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    cipher = cipher.replace(' ', '')
    decrypted = ''
    
    for k in range(0, len(cipher), blocksize(p * q)):
        plaintext = mod_exp(int(cipher[k: k + blocksize(p * q)]), modinv(e, (p - 1) * (q - 1)), p * q)
        if len(str(plaintext)) != blocksize(p * q):
            decrypted = decrypted + ('0' * (blocksize(p * q) - len(str(plaintext)))) + str(plaintext)
        else:
            decrypted += str(plaintext)
            
    return digits2letters(decrypted)
 
 
# In[78]:
 
 
# """--------------------- TESTER CELL ---------------------------"""
# decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
# decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
# decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
# print("Decrypted Message:", decrypted1)
# print("Expected: STOP")
# print("Decrypted Message:", decrypted2)
# print("Expected: HELP")
# print("Decrypted Message:", decrypted3)
# print("Expected: STOPSX")
 
# """--------------------- TEST 2---------------------------"""
# decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
# print("Decrypted Message:", decrypted)
# print("Expected: SILVER")
 
 
# ------------------------------------------
# ##### Utility functions (NO EDITS NECESSARY)
 
# In[9]:
 
 
def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters
    
 
 
# In[10]:
 
 
def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits
 
 
# In[11]:
 
 
def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
 