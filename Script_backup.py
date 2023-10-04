import os
import shutil
import time


prefix_name = time.strftime("%Y-%m-%d-%S")
path_src = os.path.abspath(r'C:\ubn\id_rsa')
path_dst = os.path.abspath(r'C:\ubn\id_rsa1')
get_name_src = os.path.basename(path_src)
create_copy_name = get_name_src + '_' + prefix_name
create_path_dst = os.path.join(path_dst, create_copy_name)

'''проверка существования исходного пути и пути назначения'''
exists_src = os.path.exists(path_src)
exists_dst = os.path.exists(path_dst)
'''проверка что исходный путь является файлом'''
exists_src_is_file = os.path.isfile(path_src)
'''если каталога назначения не существует рекурсивно создаем его '''
if exists_dst is False:
    os.makedirs(path_dst, mode=0o777, exist_ok=True)

shutil.copy2(path_src, create_path_dst)
# while True:
#     shutil.copy2(path_src, path_dst)
#     time.sleep(30)
