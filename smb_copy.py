import os
import time
from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure

username = 'ivc'
password = 'Mgmsu495!'
server_ip = '192.168.6.5'
port = 139
local_dir = os.path.abspath(r'C:\ubn\id_rsa1')
remote_dir = r"\Backup\test"
f = open('tes1.txt', 'w+')
samba = SMBConnection(username, password, '', '', use_ntlm_v2=True)
samba.connect(server_ip, port)
file_obj1 = samba.retrieveFile('Soft', '/test.txt', 'f')
# print(file_obj)
# content = samba.retrieveFile('Soft', '/')
# if content:
#     print(content.decode('utf-8'))  # декодируем содержимое файла в строку
# else:
#     print('Файл не найден')