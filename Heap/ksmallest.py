def ksmallest(arr,k):
    ls=[]
    for i in range(len(arr)):
        ls.append(arr[i])
        if len(ls)>k:
            ls.sort()
            ls.pop()
    if ls:
        ls.sort()
        return ls[k-1]
    return 0

if __name__ == "__main__":
    arr=[2,7,3,8,1,9]
    k=3
    ans= ksmallest(arr,k)

    print(ans)
