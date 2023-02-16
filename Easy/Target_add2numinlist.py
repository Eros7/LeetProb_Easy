class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lens=0
        index_list=[]
        for items in nums:
            lens+=1
            
        for i in range(lens):
            for j in range(i+1,lens,1):
                if (nums[i]+nums[j]==target):
                    index_list.append(i)
                    index_list.append(j)
                    return index_list
        return 0

arr=Solution()
indecs=arr.twoSum([1,2,3,4],7)

if indecs==0:
    print("No solution")
else:
    print(indecs)




