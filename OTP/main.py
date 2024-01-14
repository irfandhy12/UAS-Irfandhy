import pyotp

# Membuat secret key untuk OTP
secret_key = pyotp.random_base32()

# Membuat objek TOTP (Time-based OTP) dengan secret key
totp = pyotp.TOTP(secret_key)

# Menghasilkan OTP
otp = totp.now()

print("Secret Key:", secret_key)def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher_encrypt(plaintext, key):
    a, b = key
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a')) * a + b) % 26 + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A')) * a + b) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def affine_cipher_decrypt(ciphertext, key):
    a, b = key
    plaintext = ''
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Kunci tidak valid. 'a' harus saling prima dengan 26."
    
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - b) * a_inv) % 26 + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - b) * a_inv) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Ini adalah contoh pesan"
key = (3, 7)  # Contoh kunci, Anda bisa mengganti dengan kunci lain
ciphertext = affine_cipher_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = affine_cipher_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)

print("One-Time Password (OTP):", otp)
