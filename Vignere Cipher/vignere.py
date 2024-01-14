# Fungsi untuk mengenkripsi pesan menggunakan Vigenère Cipher
def encrypt(text, key):
    # Membersihkan teks dari karakter selain huruf
    text = ''.join(filter(str.isalpha, text))
    text = text.upper()  # Mengubah teks menjadi huruf besar
    key = key.upper()  # Mengubah kunci menjadi huruf besar
    encrypted_text = ""

    key_length = len(key)
    key_as_int = [ord(i) for i in key]  # Mendapatkan nilai ASCII dari kunci

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_shift = key_as_int[i % key_length] - 65  # Konversi huruf kunci ke nilai 0-25 (A=0, B=1, ..., Z=25)

            if char.isupper():
                encrypted_text += chr(((ord(char) + key_shift - 65) % 26) + 65)  # Enkripsi huruf besar
            else:
                encrypted_text += chr(((ord(char) + key_shift - 97) % 26) + 97)  # Enkripsi huruf kecil
        else:
            encrypted_text += char  # Menjaga karakter selain huruf tetap sama

    return encrypted_text

# Fungsi untuk mendekripsi pesan yang dienkripsi menggunakan Vigenère Cipher
def decrypt(text, key):
    text = text.upper()
    key = key.upper()
    decrypted_text = ""

    key_length = len(key)
    key_as_int = [ord(i) for i in key]  # Mendapatkan nilai ASCII dari kunci

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_shift = key_as_int[i % key_length] - 65  # Konversi huruf kunci ke nilai 0-25 (A=0, B=1, ..., Z=25)

            if char.isupper():
                decrypted_text += chr(((ord(char) - key_shift - 65) % 26) + 65)  # Dekripsi huruf besar
            else:
                decrypted_text += chr(((ord(char) - key_shift - 97) % 26) + 97)  # Dekripsi huruf kecil
        else:
            decrypted_text += char

    return decrypted_text

# Contoh penggunaan
pesan = "Ini adalah pesan rahasia yang akan dienkripsi"
kunci = "KUNCI"  # Kunci untuk enkripsi

pesan_terenkripsi = encrypt(pesan, kunci)
pesan_terdekripsi = decrypt(pesan_terenkripsi, kunci)

print("Pesan Asli:", pesan)
print("Pesan Terenkripsi:", pesan_terenkripsi)
print("Pesan Terdekripsi:", pesan_terdekripsi)
