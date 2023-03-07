import string
import time


class program():
    def __init__(self):

        def encrypt(message, shift):
            # create a dictionary to map letters to their ciphertext equivalents
            alphabet = string.ascii_lowercase
            cipher_map = {letter: alphabet[(index+shift)%26] for index, letter in enumerate(alphabet)}
            
            # encrypt the message by replacing each letter with its ciphertext equivalent
            ciphertext = ""
            for letter in message:
                if letter.lower() in cipher_map:
                    if letter.isupper():
                        ciphertext += cipher_map[letter.lower()].upper()
                    else:
                        ciphertext += cipher_map[letter.lower()]
                else:
                    ciphertext += letter
            
            return ciphertext

        # display the menu
        print("=== Caesar Cipher Encrypter ===")
        shift = int(input("Enter the shift value (1-25): "))
        message = input("Enter the message to encrypt: ")

        # encrypt the message
        ciphertext = encrypt(message, shift)

        # display the encrypted message
        print("Encrypted message: ", ciphertext)
        menu()



        def decrypt(ciphertext, shift):
            # create a dictionary to map ciphertext letters to their plaintext equivalents
            alphabet = string.ascii_lowercase
            cipher_map = {alphabet[(index+shift)%26]: letter for index, letter in enumerate(alphabet)}
            
            # decrypt the message by replacing each ciphertext letter with its plaintext equivalent
            plaintext = ""
            for letter in ciphertext:
                if letter.lower() in cipher_map:
                    if letter.isupper():
                        plaintext += cipher_map[letter.lower()].upper()
                    else:
                        plaintext += cipher_map[letter.lower()]
                else:
                    plaintext += letter
            
            return plaintext

        # display the menu
        print("=== Caesar Cipher Decrypter ===")
        shift = int(input("Enter the shift value (1-25): "))
        ciphertext = input("Enter the message to decrypt: ")

        # decrypt the message
        plaintext = decrypt(ciphertext, shift)

        # display the decrypted message
        print("Decrypted message: ", plaintext)
        menu()

class menu():
    def __init__(self):
        print("\n\n-----------")
        print("Operation type")
        print("  1 = Encrypt")
        print("  2 = Decrypt")
        
        

        choice = int(input("Option number: "))
        if choice == 1:
            program().encrypt()
        elif choice == 2:
            program().decrypt()
        
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            menu()
            
if __name__ == "__main__":
    menu()