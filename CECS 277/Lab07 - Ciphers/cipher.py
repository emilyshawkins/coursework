import string

class Cipher():
  '''
  Represents an Atbash Cipher

  Attributes:
  alphabet (list) : A list of all the uppercase letter in the English alphabet
  '''

  def __init__(self):
    
    self._alphabet = list(string.ascii_uppercase)

  def encrypt_message(self, message):
    '''Encrypts all the letters in the user's message using the Atbash Cipher while leaving spaces, numbers and punctuation as is.'''
    
    str = ''
    # Turns all the letters in the user's message into uppercase letters.
    message = message.upper()

    # Iterates through all the characters in the user's message and encrypts them one by one if they are a letter.
    for char in message:
      if char in self._alphabet:
        encrypt = self._encrypt_letter(char)
      elif char not in self._alphabet:
        encrypt = char

      str += encrypt
      
    return str

  def decrypt_message(self, message):
    '''Decrypts all the letters in the user's message using the Atbash Cipher while leaving spaces, numbers and punctuation as is.'''

    str = ''
    # Turns all the letters in the user's message into uppercase letters.
    message = message.upper()

    # Iterates through all the characters in the user's message and decrypts them one by one if they are a letter.
    for char in message:
      if char in self._alphabet:
        decrypt = self._decrypt_letter(char)
      elif char not in self._alphabet:
        decrypt = char

      str += decrypt
      
    return str


  def _encrypt_letter(self, letter):
    '''Finds the location of the letter from the user's message in the alphabet and uses that location to calculate the location of the encrypted letter in Atbash and returns the encrypted letter.'''

    location = 0
    # Finds the location of the letter in the alphabet list.
    for i in range(len(self._alphabet)):
      if letter == self._alphabet[i]:
        location = i
        break

    # Calculates the location of the encrypted letter.
    encrypted = self._alphabet[25 - location]

    return encrypted 

  def _decrypt_letter(self, letter):
    '''Finds the location of the letter from the Atbash encrypted message in the alphabet and uses that location to calculate the location of the decrypted letter and returns the decrypted letter.'''
    
    location = 0
    # Finds the location of the letter in the alphabet list.
    for i in range(len(self._alphabet)):
      if letter == self._alphabet[i]:
        location = i
        break

    # Calculates the location of the decrypted letter.
    decrypted = self._alphabet[25 - location]

    return decrypted 
