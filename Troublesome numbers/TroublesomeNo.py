def merge(left, right):
    return sorted(left + right)


def recursion(arr):
    if len(arr) <= 1:
        return 0, arr
    half = len(arr) // 2
    left_ans, left = recursion(arr[:half])
    right_ans, right = recursion(arr[half:])
    cross_ans = 0
    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        cross_ans += j
    return left_ans + cross_ans + right_ans , merge(left, right)

n = int(input())
m = list(map(int,input().strip().split()))[:n] 
print(recursion(m)[0] )