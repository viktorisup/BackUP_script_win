# # import os
# # import time
# # from smb.SMBConnection import SMBConnection
# # from smb.smb_structs import OperationFailure
# #
# # username = 'ivc'
# # password = 'Mgmsu495!'
# # server_ip = '192.168.6.5'
# # port = 139
# # local_dir = os.path.abspath(r'C:\ubn\id_rsa1')
# # remote_dir = r"\Backup\test"
# #
# #
# # class MySMB:
# #
# #     def __init__(self, username, password, server_ip, port):
# #         self.samba = SMBConnection(
# #             username, password, '', '', use_ntlm_v2=True)
# #         self.samba.connect(server_ip, port)
# #         self.service_name = "Disk1share"
# #
    def upload_files(self, local_dir, smb_base_dir: str):
        for root, dir_list, file_list in os.walk(local_dir):
            self.samba.createDirectory(self.service_name, smb_base_dir)
            smb_root = os.path.join(smb_base_dir, root.replace(
                local_dir, "").lstrip("/"))
            for dir_name in dir_list:
                smb_dir = os.path.join(smb_root, dir_name)
                # print("smb_dir: ",smb_dir)
                self.samba.createDirectory(self.service_name, smb_dir)
            for file_name in file_list:
                if file_name.endswith(".sock"):
                    continue
                smb_path = os.path.join(smb_root, file_name)
                local_path = os.path.join(root, file_name)
                modify_time = os.path.getmtime(local_path)
                with open(local_path, 'rb') as f:
                    self.samba.storeFile(
                        self.service_name, smb_path, f, timeout=3000)
# #
# #
# # smb_obj = MySMB(username, password, server_ip, port)
# # try:
# #     smb_obj.upload_files(local_dir, remote_dir)
# # except Exception as e:
# #     print(e)
# # finally:
# #     smb_obj.samba.close()
#
# import os
# from smb.SMBConnection import SMBConnection
#
#
# def copy_folder_to_smb(local_folder_path, remote_folder_path, server_ip, username, password, client_name, server_name,
#                        share_name):
#     conn = SMBConnection(username, password, client_name, server_name, use_ntlm_v2=True)
#     conn.connect(server_ip, 445)
#     print(conn.isUsingSMB2)
#
#     for root, dirs, files in os.walk(local_folder_path):
#         for file in files:
#             local_file_path = os.path.join(root, file)
#             remote_file_path = os.path.join(remote_folder_path, file)
#
#             with open(local_file_path, 'rb') as local_file:
#                 conn.storeFile(share_name, remote_file_path, local_file)
#
#     print("Папка успешно скопирована на SMB-сервер!")
#     conn.close()
#
#
# # Пример использования функции
# local_folder_path = 'C:/ubn/'
# remote_folder_path = '/test/'
# server_ip = '192.168.6.5'
# username = 'ivc'
# password = 'Mgmsu495!'
# client_name = 'msmsu-isupov64'
# server_name = 'msmsu-smb'
# share_name = 'IVC-Doc'
#
# copy_folder_to_smb(local_folder_path, remote_folder_path, server_ip, username, password, client_name, server_name,
#                    share_name)