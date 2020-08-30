
def bubble_sort(data_lst: list):
    size = len(data_lst)
    # 这里-1是因为最后一个数字不需要遍历，肯定是最小的
    for i in range(size - 1):
        # 这里-i的原因是最后排好序的拿i个元素，不需要再排序了
        # 这里-1的愿意是因为是第j个和第j+1个做对比，所以不需要对最后一个（j+1）遍历
        for j in range(size - i - 1):
            if data_lst[j] > data_lst[j + 1]:
                data_lst[j], data_lst[j + 1] = data_lst[j + 1], data_lst[j]

    return data


if __name__ == '__main__':
    data = [1, 4, 6, 8, 3]
    p = bubble_sort(data)
    print(p)
