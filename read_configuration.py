def read_conf():
    conf_dict = {}
    with open('conf.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] == '#' or line == '\n':
                continue
            if 'src_path' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
            if 'ip_srv' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
            if 'remote_name' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
                if conf_dict[key] == 'None':
                    conf_dict[key] = ''
            if 'domain' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
                if conf_dict[key] == 'None':
                    conf_dict[key] = ''
            if 'smb_root_dir' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
            if 'smb_base_dir' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
                if conf_dict[key] == 'None':
                    conf_dict[key] = ''
            if 'login' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]
            if 'passwd' in line:
                key, value = line.split(' = ')
                conf_dict[key] = value[:-1]

    return conf_dict

