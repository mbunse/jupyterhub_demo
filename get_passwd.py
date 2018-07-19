import hmac
import hashlib


secret_key = bytearray.fromhex("my secret hey key")
username = "username".encode('utf-8')
password = hmac.new(secret_key, username, hashlib.sha512).hexdigest()
print(password)
