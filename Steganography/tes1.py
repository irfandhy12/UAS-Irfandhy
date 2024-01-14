from PIL import Image

def encode_image(image_path, message, output_path):
    # Baca gambar
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Ubah pesan menjadi biner
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Sisipkan panjang pesan pada delapan bit pertama gambar
    binary_message_length = format(len(binary_message), '08b')
    pixels[0] = tuple(int(pixel[:8] + binary_message_length[i*8:(i+1)*8], 2) for i, pixel in enumerate(pixels[0]))

    # Sisipkan pesan dalam gambar
    for i in range(len(binary_message)):
        pixels[i+1] = tuple(int(pixel[:7] + binary_message[i], 2) + int(pixel[7:], 2) for pixel in pixels[i+1])

    # Simpan gambar baru yang berisi pesan tersembunyi
    encoded_img = Image.new('RGB', img.size)
    encoded_img.putdata(pixels)
    encoded_img.save(output_path)

    print("Pesan berhasil disisipkan dalam gambar.")

def decode_image(image_path):
    # Baca gambar
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Ambil panjang pesan dari delapan bit pertama gambar
    binary_message_length = ''.join(format(pixel[0], '08b') for pixel in pixels[0])
    message_length = int(binary_message_length, 2)

    # Ambil pesan dari gambar
    binary_message = ''.join(format(pixel[7], '01b') for pixel in pixels[1:message_length+1])

    # Konversi pesan biner ke string
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return message

# Contoh penggunaan
image_path = cat.jpg
output_path = cat.jpg
message_to_hide = "Ini adalah pesan rahasia!"

# Sisipkan pesan dalam gambar
encode_image(image_path, message_to_hide, output_path)

# Dekode pesan dari gambar
decoded_message = decode_image(output_path)
print("Pesan yang tersembunyi dalam gambar:", decoded_message)
