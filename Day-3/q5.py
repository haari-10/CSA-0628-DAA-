def findKthPositive(arr,k):
    cur=1
    i=0
    while k>0:
        if i<len(arr) and arr[i]==cur:
            i+=1
        else:
            k-=1
            if k==0:
                return cur
        cur+=1

print(findKthPositive([2,3,4,7,11],5))