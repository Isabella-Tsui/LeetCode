class MayjorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        numsInList = {}
        for num in nums:
            if num not in numsInList:
                numsInList[num] = 0
            
            numsInList[num] += 1
        
        highestFrequency = 0
        majorityElement = 0
        for num in numsInList:
            if numsInList[num] > highestFrequency:
                highestFrequency = numsInList[num]
                majorityElement = num
        
        return majorityElement