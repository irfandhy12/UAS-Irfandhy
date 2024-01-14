def enkripsi_poli(plaintext, kunci1, kunci2):
    ciphertext = ""
    index = 0

    for karakter in plaintext:
        if karakter.isalpha():
            if karakter.islower():
                offset = ord('a')
            else:
                offset = ord('A')

            if index % 2 == 0:
                key = ord(kunci1[index % len(kunci1)]) - offset
            else:
                key = ord(kunci2[index % len(kunci2)]) - offset

            encrypted_char = chr(((ord(karakter) - offset + key) % 26) + offset)
            ciphertext += encrypted_char
            index += 1
        else:
            ciphertext += karakter

    return ciphertext

# Contoh penggunaan
pesan = "BELAJAR KRIPTOGRAFI"
kunci1 = "MERDEKA"
kunci2 = "INDONESIA"

pesan_terenkripsi = enkripsi_poli(pesan, kunci1, kunci2)
print("Pesan terenkripsi:", pesan_terenkripsi)
