class Substitute_Cipher:
  def generate_key(self):
    """Generates a random key for the cipher."""
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return ''.join(shuffled_alphabet)

  def encrypt(self, message, key):
    """Encrypts a message using the given key."""
    cipher = ''
    for char in message:
      if char.isalpha():
        index = ord(char.lower()) - ord('a')
        new_char = key[index]
        cipher += new_char.upper() if char.isupper() else new_char
      else:
        cipher += char
    return cipher

  def decrypt(self, ciphertext, key):
    """Decrypts a ciphertext using the given key."""
    message = ''
    for char in ciphertext:
      if char.isalpha():
        index = key.find(char.upper()) if char.isupper() else key.find(char.lower())
        new_char = chr(index + ord('a'))
        message += new_char
      else:
        message += char
    return message

  # def main():
  #   """Prompts user for input and performs encryption/decryption."""
  #   print("Welcome to the Substitution Cipher!")
  #   choice = input("Do you want to encrypt (e) or decrypt (d)? ").lower()
  #   if choice not in ('e', 'd'):
  #     print("Invalid choice. Please enter 'e' or 'd'.")
  #     return
  #
  #   if choice == 'e':
  #     message = input("Enter the message to encrypt: ")
  #     key = generate_key()
  #     print("Generated key:", key)
  #     ciphertext = encrypt(message, key)
  #     print("Encrypted message:", ciphertext)
  #   else:
  #     ciphertext = input("Enter the ciphertext to decrypt: ")
  #     key = input("Enter the secret key (optional, leave blank if unknown): ")
  #     if not key:
  #       print("Attempting to decrypt without key...")
  #     decrypted_message = decrypt(ciphertext, key)
  #     print("Decrypted message:", decrypted_message)
