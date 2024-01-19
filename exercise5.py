def bubble_sort(arr):
    n = len(arr)
    while n > 1:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                flag = True
        n -= 1
        if not flag:
            break
    return arr
