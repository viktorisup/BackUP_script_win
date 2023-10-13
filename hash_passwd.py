from cryptography.fernet import Fernet

user_login = 'isupov'
user_passwd = 'Mgmsu495!'
key = Fernet.generate_key()
key2 = b'Mgmsu!'
fernet = Fernet(key)
encrypt_str = fernet.encrypt(user_passwd.encode())
decrypt_str = fernet.decrypt(user_passwd).decode()
print(encrypt_str)