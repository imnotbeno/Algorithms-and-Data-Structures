#Bubble sort algorithm exercise

l = [5, 1, 4, 2, 8]

def bubble_sort(arr):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

bubble_sort(l)

for i in range(len(l)):
    print(l[i])
