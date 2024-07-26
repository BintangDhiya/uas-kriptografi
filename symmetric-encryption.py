from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Fungsi untuk enkripsi menggunakan AES
def encrypt_aes(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv, ct_bytes

# Fungsi untuk dekripsi menggunakan AES
def decrypt_aes(iv, cipher_text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return pt.decode()

# Contoh penggunaan
key = get_random_bytes(16)  # AES membutuhkan kunci sepanjang 16 bytes
plain_text = "Ini adalah teks rahasia"
iv, cipher_text = encrypt_aes(plain_text, key)
decrypted_text = decrypt_aes(iv, cipher_text, key)

print("Teks asli:", plain_text)
print("Teks terenkripsi:", cipher_text)
print("Teks terdekripsi:", decrypted_text)
