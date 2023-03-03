import sys
import base64
from Crypto.Cipher import AES

def decrypt_aes(key, iv, data):
    key = base64.b64decode(key)
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data).decode("utf-8")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Palo Alto Firewall config secrets decryptor')
        print('Usage: python mkdecrypt.py [base64_data]')
        sys.exit(1)

    key = 'gQOFAkW5tI8EKMW3TiYVUoEDhQJFubSPBCjFt04mFVI='
    iv = b'\0'*16
    data = sys.argv[1]

    decrypted_data = decrypt_aes(key, iv, data)
    print('Decrypted data:\r\n\r\n{}'.format(decrypted_data))
