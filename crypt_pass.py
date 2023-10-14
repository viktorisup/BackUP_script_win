from cryptography.fernet import Fernet


def decrypter(val):
    key = b'b5Yiml3-bQzEPiWRdXO4Fyc194gSbLC6OIr444zifpA='
    fer = Fernet(key)
    decrypt_str = fer.decrypt(val).decode()
    return decrypt_str


if __name__ == '__main__':
    user_login = input('Введите логин для шифрования: ')
    user_passwd = input('Введите пароль для шифрования: ')
    key = b'b5Yiml3-bQzEPiWRdXO4Fyc194gSbLC6OIr444zifpA='

    fer = Fernet(key)

    with open('pass_encrypt.txt', 'w', encoding='utf-8') as f:
        encrypt_login = fer.encrypt(user_login.encode())
        encrypt_passwd = fer.encrypt(user_passwd.encode())
        print(type(encrypt_login))
        f.write('Логин' + '\n' + encrypt_login.decode() + '\n')
        f.write('Пароль' + '\n' + encrypt_passwd.decode())
