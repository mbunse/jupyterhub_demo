import hmac
import hashlib
import yaml
import secrets

config = None
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

config["proxy"]["secretToken"] = secrets.token_hex(32)
config["auth"]["hmac"]["secretKey"] = secrets.token_hex(64)

secret_key = bytearray.fromhex(config["auth"]["hmac"]["secretKey"])
for username in config["auth"]["whitelist"]["users"]:
    username_utf8 = username.encode('utf-8')
    password = hmac.new(secret_key, username_utf8, hashlib.sha512).hexdigest()
    print(username, password)

with open("build/config.yaml", "w") as f:
    yaml.dump(config, f)

