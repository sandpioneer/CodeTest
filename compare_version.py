from itertools import zip_longest


def compareVersion(version1: str, version2: str) -> int:
    v = zip_longest(version1.split('.'), version2.split('.'), fillvalue=0)
    v = list(v)
    for i in range(len(v)):
        if int(v[i][0]) > int(v[i][1]):
            return 1
        elif int(v[i][0]) < int(v[i][1]):
            return -1

    return 0
