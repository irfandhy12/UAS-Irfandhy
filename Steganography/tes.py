from stegano import lsb
secret = lsb.hide("cat.jpg","universitas pelita bangsa")
secret.save("cat-sec.png")
print(lsb.reveal("cat-sec.png"))