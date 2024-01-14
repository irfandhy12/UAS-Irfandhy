from PIL import Image, ImageDraw, ImageFont

def sisipkan_teks_gambar(nama_file, teks):
    # Buka gambar
    img = Image.open(nama_file)
    
    # Inisialisasi ImageDraw untuk menggambar teks
    draw = ImageDraw.Draw(img)
    
    # Ukuran font dan teks yang akan disisipkan
    font = ImageFont.truetype("arial.ttf", 50)  # Ganti font dan ukurannya sesuai kebutuhan
    text_color = (255, 255, 255)  # Warna teks (RGB)

    # Tentukan posisi teks
    text_position = (20, 20)  # Koordinat teks pada gambar
    
    # Sisipkan teks ke dalam gambar
    draw.text(text_position, teks, fill=text_color, font=font)
    
    # Simpan gambar yang telah dimodifikasi
    img.save("gambar_dengan_teks.png")

# Gunakan fungsi untuk menyisipkan teks pada gambar
nama_file_gambar = "Cyber.jpg"  #gambar yang di sisipkan
pesan = "Saya Mahassiswa Informatika" #Pesan yang disisipkan

#sisipkan_teks_gambar(nama_file_gambar, pesan)