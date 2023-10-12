import os
import time
from smb.SMBConnection import SMBConnection
from read_configuration import read_conf


class MySMB:

    def __init__(self, username, password, server_ip, port, local_dir, smb_base_dir, smb_dir):
        self.backup_folder = 'Backup_' + os.path.basename(local_dir) + '_' + time.strftime("%Y-%m-%d-%S")
        self.local_dir = os.path.abspath(local_dir)
        self.smb_base_dir = smb_base_dir
        self.smb_dir_src = smb_dir
        self.smb_dir = os.path.join(smb_dir, self.backup_folder)
        self.name_file = os.path.basename(local_dir)
        self.samba = SMBConnection(username, password, '', 'win-ad', use_ntlm_v2=True)
        self.samba.connect(server_ip, port)

    def upload_files(self):
        self.samba.createDirectory(self.smb_base_dir, self.smb_dir)
        self.smb_dir = os.path.join(self.smb_dir, self.name_file)
        with open(self.local_dir, 'rb') as file:
            self.samba.storeFile(self.smb_base_dir, self.smb_dir, file)
            print("Файл успешно скопирован на SMB-сервер!")

    def upload_folder(self):
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


if __name__ == "__main__":

    cfg_dict = read_conf()

    list_keys = list(cfg_dict)
    list_num = []

    for j in list_keys:
        if j[-1].isdigit():
            list_num.append(j[-1])

    max_num = 1
    if len(list_num) > 0:
        max_num = int(max(list_num))

    idx = 1
    while idx <= max_num:
        if idx == 1:
            loc_dir_c = cfg_dict['src_path']
            srv_ip_c = cfg_dict['ip_srv']
            smb_root_dir_c = cfg_dict['smb_root_dir']
            smb_dir_after_root_c = cfg_dict['smb_base_dir']
            login_c = cfg_dict['login']
            passwd_c = cfg_dict['passwd']
            prt = 139

            smb_obj = MySMB(login_c, passwd_c, srv_ip_c, prt, loc_dir_c, smb_root_dir_c, smb_dir_after_root_c)
            try:
                if os.path.isfile(loc_dir_c) is True:
                    smb_obj.upload_files()
                else:
                    smb_obj.upload_folder()
            except Exception as e:
                print(e)
            finally:
                smb_obj.samba.close()
            idx += 1
        else:
            loc_dir_c = cfg_dict['src_path' + str(idx)]
            srv_ip_c = cfg_dict['ip_srv' + str(idx)]
            smb_root_dir_c = cfg_dict['smb_root_dir' + str(idx)]
            smb_dir_after_root_c = cfg_dict['smb_base_dir' + str(idx)]
            login_c = cfg_dict['login' + str(idx)]
            passwd_c = cfg_dict['passwd' + str(idx)]
            prt = 139

            smb_obj = MySMB(login_c, passwd_c, srv_ip_c, prt, loc_dir_c, smb_root_dir_c, smb_dir_after_root_c)
            try:
                if os.path.isfile(loc_dir_c) is True:
                    smb_obj.upload_files()
                else:
                    smb_obj.upload_folder()
            except Exception as e:
                print(e)
            finally:
                smb_obj.samba.close()
            idx += 1
