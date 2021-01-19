# !python3

l = [10, 80, 30, 90, 50, 60, 40, 20, 70]
n = len(l)

def partitioning(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):
        if   arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) #return pivot index

def quickSort(arr,low,high):
    if low < high:
        pi = partitioning(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(l,0,n-1)
print("Sorted array: ")
for x in range(n):
    print(l[x])
