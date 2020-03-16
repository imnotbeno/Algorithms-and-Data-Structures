#Binary Searching for the index of a wanted element

# Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
# Begin with an interval covering the whole array. If the value of the search key is less
# than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise narrow it to the upper half. Repeatedly check until the value is found or
# the interval is empty


"""
def binSearch(arr, l, s, num):
    m = (l-s)//2 #Array length minus the start divided by two

    if arr[m] == num:
        return m
    elif arr[m] > num:
        return binSearch(arr, m - 1, s, num)
    else:
        return binSearch(arr, l, m + 1, num)

arr1 = [23, 12, 63, 72, 1, 48, 938, 1654, 536, 123]

a = sorted(arr1)
l = len(arr1)
x =int(input("Search for value: "))

bin = binSearch(a, l - 1, 0, x)

print("Your value is at index: ", bin)
"""

def binarySearch (arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l)//2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = int(input("Which element: "))

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element at: ", result)
else:
    print("Element is not present in array")
