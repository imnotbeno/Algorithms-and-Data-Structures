# !python3
# divide and conquer algorithm

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Merge sort for the left half
        mergesort(left)
        # Merge sort for the right half
        mergesort(right)

        i= j= k= 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] < right[j]
                j+=1
            k+=1

        # Checking if any elements remain
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print()

if __name__ == "__main__":
    a = [12, 11, 13, 5, 6, 7]
    l = [3, 1, 8, 5, 10, 9, 7, 6, 4, 2]
    printList(a)
    mergesort(a)
    printList(a)

#left = l[:m]
#right = l[m:]
#print(left)
#print(right)
