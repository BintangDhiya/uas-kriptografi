from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Fungsi untuk menghasilkan kunci RSA
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Fungsi untuk enkripsi menggunakan RSA
def encrypt_rsa(plain_text, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(plain_text.encode())

# Fungsi untuk dekripsi menggunakan RSA
def decrypt_rsa(cipher_text, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(cipher_text).decode()

# Contoh penggunaan
private_key, public_key = generate_rsa_keys()
plain_text = "Ini adalah teks rahasia"
cipher_text = encrypt_rsa(plain_text, public_key)
decrypted_text = decrypt_rsa(cipher_text, private_key)

print("Teks asli:", plain_text)
print("Teks terenkripsi:", cipher_text)
print("Teks terdekripsi:", decrypted_text)
