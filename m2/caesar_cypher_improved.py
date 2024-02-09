# Caesar cipher.
def encrypt():
    text = input("Enter your message: ")
    scale = input("Enter the shift value (0 to 25): ")
    while(scale.isdigit() == False or int(scale) > 25): scale = input("Enter the shift value (0 to 25): ")
    cipher = ''
    for char in text:
        if not char.isalpha(): continue
        _char = char.upper()
        code = ord(_char) + int(scale)
        if code > ord('Z'): code = ord('A')
        if char.capitalize() != char: cipher += chr(code).lower()
        else: cipher += chr(code)

    return cipher, scale

def decrypt(cipher, scale):
    text = ''
    for char in cipher:
        if not char.isalpha(): continue
        _char = char.upper()
        code = ord(_char) - int(scale)
        if code < ord('A'): code = ord('Z')
        if char.capitalize() != char: text += chr(code).lower()
        else: text += chr(code)

    return text


if __name__ == "__main__":
    cipher, scale = encrypt()
    text = decrypt(cipher, scale)

    print(f"Cipher text: {cipher}")
    print(f"Original text: {text}")
