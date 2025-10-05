# caesar_cipher.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # check if it's a letter
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # keep spaces and symbols same
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # just reverse the shift


# Main part of program
print("=== Caesar Cipher Encryption & Decryption ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print(f"\nEncrypted Message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted Message: {decrypted}")
