import os
import time
from smb.SMBConnection import SMBConnection


class MySMB:

    def __init__(self, username, password, server_ip, port, local_dir, smb_base_dir, smb_dir):
        self.backup_folder = 'Backup_' + os.path.basename(local_dir) + '_' + time.strftime("%Y-%m-%d-%S")
        self.local_dir = os.path.abspath(local_dir)
        self.smb_base_dir = smb_base_dir
        self.smb_dir_src = smb_dir
        self.smb_dir = os.path.join(smb_dir, self.backup_folder)
        self.name_file = os.path.basename(local_dir)
        self.samba = SMBConnection(username, password, '', '', use_ntlm_v2=True)
        self.samba.connect(server_ip, port)

    def upload_files(self):
        self.samba.createDirectory(self.smb_base_dir, self.smb_dir)
        self.smb_dir = os.path.join(self.smb_dir, self.name_file)
        with open(self.local_dir, 'rb') as file:
            self.samba.storeFile(self.smb_base_dir, self.smb_dir, file)
            print("Файл успешно скопирован на SMB-сервер!")

    def upload_folder(self):
        # self.samba.createDirectory(self.smb_base_dir, self.smb_dir)
        for root, dir_list, file_list in os.walk(self.local_dir):
            walk_dir_tmp = root.split(self.local_dir)[1]
            walk_dir_tmp = walk_dir_tmp[1:]
            walk_dir = os.path.join(self.smb_dir, walk_dir_tmp)
            self.samba.createDirectory(self.smb_base_dir, walk_dir)
            for i in file_list:
                item = os.path.join(root, i)
                item_smb = item.split(self.local_dir)[1]
                item_smb_join = os.path.join(self.backup_folder, item_smb[1:])
                with open(item, 'rb') as file:
                    if self.smb_dir_src == '':
                        self.samba.storeFile(self.smb_base_dir, item_smb_join, file)
                    else:
                        self.samba.storeFile(self.smb_base_dir, os.path.join(self.smb_dir_src, item_smb_join), file)
        print("Папка успешно скопирован на SMB-сервер!")


login = 'ivc'
passwd = '12345678'
srv_ip = '192.168.55.4'
prt = 139
loc_dir = r'C:\ubn'
smb_root_dir = 'ivc folders'
smb_dir_after_root = r'\test\test2'


# for root, dir, file in os.walk(loc_dir):
#     print(root)

if __name__ == "__main__":
    smb_obj = MySMB(login, passwd, srv_ip, prt, loc_dir, smb_root_dir, smb_dir_after_root)
    try:
        smb_obj.upload_folder()
    except Exception as e:
        print(e)
    finally:
        smb_obj.samba.close()




