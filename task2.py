def find_kth_smallest(arr: list[int], k: int) -> int:
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)

    if k < len(left):
        return find_kth_smallest(left, k)
    elif k > len(left) + 1:
        return find_kth_smallest(right, k - len(left) - 1)
    else:
        return pivot

if __name__ == '__main__':
    array = [38, -5, 12, 66, 11, -4, -20, 10, -80, -5, 11, 66, 18, -14, -20, 6, -10]
    elem = find_kth_smallest(array, 7)
    print(elem)