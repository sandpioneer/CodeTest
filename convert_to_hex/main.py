# convert str to hex


def convert_to_hex(str_pn):
    if len(str_pn) == 12:
        class_code = str_pn[0:2]
        base_num = str_pn[3:9]
        version_num = str_pn[10:12]
        hex_class_code = hex(int(class_code))[2:].zfill(2)
        hex_base_num = hex(int(base_num))[2:].zfill(6)
        hex_version_num = hex(int(version_num))[2:].zfill(2)
        return ' '.join([hex_class_code, hex_base_num[0:2], hex_base_num[2:4],
                         hex_base_num[4:6], hex_version_num])
    elif len(str_pn) == 11:
        class_code = str_pn[0:2]
        base_num = str_pn[3:8]
        version_num = str_pn[9:11]
        hex_class_code = hex(int(class_code))[2:].zfill(2)
        hex_base_num = hex(int(base_num))[2:].zfill(4)
        hex_version_num = hex(int(version_num))[2:].zfill(2)
        return ' '.join([hex_class_code, hex_base_num[0:2],
                         hex_base_num[2:4], hex_version_num])
    else:
        raise Exception('len of str_pn is not 11 or 12')


if __name__ == '__main__':
    pass
