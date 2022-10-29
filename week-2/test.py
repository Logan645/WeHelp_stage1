def maxZeros(nums):
    list=[]
    j=0
    for i in nums:
        if j>0 and i==0 and nums[j-1]==0:
            list.append(nums[j])
            j+=1
        else:
            j+=1
    if nums[0]==0 and len(list)>0:
        print(len(list)+1)
    elif len(list)>0:
         print(len(list))
    else:
        print(0)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3


maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]) # 得到 6


