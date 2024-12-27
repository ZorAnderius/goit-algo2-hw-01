def min_max(arr: list[int]) -> tuple[int, int]:
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])

    mid = len(arr) // 2
    left = min_max(arr[:mid])
    right = min_max(arr[mid:])

    return min(left[0], right[0]), max(left[1], right[1])

if __name__ == '__main__':
    array = [38, -5, 12, 66, 11, -4, -20, 10, -80]
    min_val, max_val = min_max(array)
    print(f"Min: {min_val}, Max: {max_val}")