# Q4. 최빈값이 2개 이상일 때에는 리스트를 출력하는 함수를 만들어 봅시다.
from collections import Counter


def mode(x):
    cnt = Counter(x)

    # print(cnt)
    # print(cnt.items())
    # print(cnt.keys())
    # print(cnt.values())
    cnt_max = max(cnt.values())
    # print(cnt_max)
    mode = []
    for i in cnt:
        if cnt[i] == cnt_max:
            mode.append(i)
    if len(mode) == 1:
        return mode[0]
    else:
        return mode
