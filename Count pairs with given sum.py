def getpair(arr,arrlen,sum):
    hashmap=[0]*(max(arr)+1+abs(min(arr)))
    for i in range(arrlen):
        hashmap[arr[i]]=hashmap[arr[i]]+1
        
    print(hashmap)
    
    counter=0
    for i in range(arrlen):
        counter=counter+hashmap[sum-arr[i]]
        if sum/2 == arr[i]:
            counter-=1
    return counter/2


arr=[1,5,8,-2,5]
print(int(getpair(arr,len(arr),6)))
