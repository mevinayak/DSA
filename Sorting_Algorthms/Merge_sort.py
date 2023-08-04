def merge_sort(num):
    l= len(num)
    if l<=1:
        return num
    mid= l//2
    left= num[mid:]
    right=num[:mid]
    left= merge_sort(left)
    right= merge_sort(right)

    i=j=k=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            num[k]= left[i]
            i=i+1
        else:
            num[k]= right[j]
            j=j+1
        k=k+1
    
    while i < len(left):
        num[k]=left[i]
        i=i+1
        k=k+1
    while j< len(right):
        num[k]= right[j]
        j=j+1
        k=k+1

    return num
num=[2, 7, 1, 4, 9, 3, 5, 6, 10]
s= merge_sort(num)
print(s)
