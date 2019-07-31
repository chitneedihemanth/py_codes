def get_pair_for_given_sum(arr,sum,length):
    hashset=set()
    for i in range(length):
        pass
    i=0
    for i in range(length):
        temp=sum-arr[i]
        if temp in hashset:
            print("{} {}".format(arr[i],temp))
        hashset.add(arr[i])
    

arr=[2,4,45,6,10,8]
get_pair_for_given_sum(arr,10,len(arr))