# Caesar cipher.
def encrypt():
    text = input("Enter your message: ")
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    return cipher

def decrypt(cipher):
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

    return text


if __name__ == "__main__":
    cipher = encrypt()
    text = decrypt(cipher)

    print(f"Cipher text: {cipher}")
    print(f"Original text: {text}")
