from cipher import Cipher

class Caesar_Cipher(Cipher):
  '''
  Represents a Caesar Cipher

  Attributes:
  alphabet (list) : A list of all the uppercase letter in the English alphabet
  shift (int) : An integer that designates how far the encryption alphabet is shifted from the original
  '''

  def __init__(self, shift):
    
    super().__init__()

    # Checks if the user inputted a valid shift value.
    if type(shift) is int:
      self._shift = shift
    else:
      raise ValueError('Shift must be an integer.')

  def _encrypt_letter(self, letter):
    '''Finds the location of the letter from the user's message in the alphabet and uses that location to calculate the location of the encrypted letter in Caesar and returns the encrypted letter.'''
    
    location = 0
    # Finds the location of the letter in the alphabet list.
    for i in range(len(self._alphabet)):
      if letter == self._alphabet[i]:
        location = i
        break

    # Calculates the location of the encrypted letter.
    encrypted = self._alphabet[(location + self._shift) % len(self._alphabet)]
    
    return encrypted

  def _decrypt_letter(self, letter):
    '''Finds the location of the letter from the Caesar encrypted message in the alphabet and uses that location to calculate the location of the decrypted letter and returns the decrypted letter.'''
    
    location = 0
    # Finds the location of the letter in the alphabet list.
    for i in range(len(self._alphabet)):
      if letter == self._alphabet[i]:
        location = i
        break

    # Calculates the location of the decrypted letter.
    decrypted = self._alphabet[(location - self._shift) % len(self._alphabet)]
        
    return decrypted

