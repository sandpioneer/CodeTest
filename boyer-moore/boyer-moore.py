# 字符串匹配算法,使用起来要比KMP算法更简单,更有效率

import time


def boyer_moore():
    src = 'HERE IS A SIMPLE EXAMPLE'
    tar = 'EXAMPLE'
    if len(tar) > len(src):
        return
    count = 0
    last = pointer = index = len(tar) - 1
    while pointer < len(src):
        count += 1
        # time.sleep(1.5)
        print('last =    {} -> [{}]'.format(src[last], last))
        print('pointer = {} -> [{}]'.format(src[pointer], pointer))
        print('index =   {} -> [{}]'.format(tar[index], index))
        if src[pointer] == tar[index]:
            pointer -= 1
            index -= 1
            if index < 0:
                return True
        else:
            if src[pointer] in tar:
                move = index - tar.index(src[pointer])
                move = move if move > 0 else 1
                last += move
            else:
                last += index + 1
            pointer = last
            index = len(tar) - 1

        print('compared times is', str(count))


def get_last_index(parameter_list):
    pass


if __name__ == '__main__':
    if not boyer_moore():
        print('tar is not in src')
    else:
        print('tar is in src')
