# Megan Waples and Emily Hawkins
# Fall 2022
# Allows the user to encrypt or decrypt messages using different types of encryption methods.

import cipher
import caesar_cipher
import check_input

def main():

  # Checks if user wants to encrypt or decrypt a message.
  user_input = check_input.get_int_range('Secret Decoder Ring: \n   1. Encrypt \n   2. Decrypt\n', 1, 2)

  if user_input == 1:

    # Checks how the user wants to encrypt their message.
    user_type = check_input.get_int_range('Enter encryption type:\n   1. Atbash\n   2. Caesar\n', 1, 2)
    user_message = input('Enter message: ')

    if user_type == 1:
      # Encrypts using Atbash.
      user_cipher = cipher.Cipher()
      encrypted = user_cipher.encrypt_message(user_message)

    else:
      # Encrypts using Caesar.
      user_shift = check_input.get_int_range('Enter shift value (0 - 25): ', 0, 25)
      user_cipher = caesar_cipher.Caesar_Cipher(user_shift)
      encrypted = user_cipher.encrypt_message(user_message)

    # Writes to text file.
    file = open("message.txt", "w")
    file.write(encrypted)

    print('Encrypted message saved to "message.txt".')


  else:

    # Checks how the user wants to decrypt their message.
    user_type = check_input.get_int_range('Enter decryption type:\n   1. Atbash\n   2. Caesar\n', 1, 2)

    # Reads from text file.
    file = open("message.txt")
    user_message = file.read()

    if user_type == 1:
      # Decrypts using Atbash.
      user_cipher = cipher.Cipher()
      decrypted = user_cipher.decrypt_message(user_message)
      
    else:
      # Decrypts using Caesar.
      user_shift = check_input.get_int_range('Enter shift value (0 - 25): ', 0, 25)
      user_cipher = caesar_cipher.Caesar_Cipher(user_shift)
      decrypted = user_cipher.decrypt_message(user_message)

    print('Reading message from "message.txt".')
    print(f'Decrypted message: {decrypted}')

main()