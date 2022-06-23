def isMaxheap(arr,i,n):
    if i >= int((n - 1) / 2):
        return True
    
    if(arr[i] > arr[2 * i + 1] and
       arr[i] > arr[2 * i + 2] and
       isMaxheap(arr, 2 * i + 1, n) and
       isMaxheap(arr, 2 * i + 2, n)):
        return True
     
    return False

n = int(input())
arr = list(map(int,input().strip().split()))[:n]

for k in range(len(arr)) :
    j = n - k - 1
    if arr[j] == -1:
        if 2*j+1 >= n :
            arr[j] = 1
        else:
            if 2*j+2 >= n:
                arr[j] = arr[2*j+1] + 1
            else : 
                arr[j] = max(arr[2*j+1] , arr[2*j+2]) + 1

if isMaxheap(arr, 0, n-1):
    print(*arr)

else:
    print("Failed")
