def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubbledes(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr
arr = [1, 5, 2, 7, 3, 8]
a = bubble(arr)
b= bubbledes(arr)
print(a,b)