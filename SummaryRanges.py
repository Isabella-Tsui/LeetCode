class SummaryRanges:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        startRange = nums[0]
        endRange = None
        windowStart = 0
        windowEnd = 1
        result = []

        while windowEnd < len(nums):
            if nums[windowStart] + 1 == nums[windowEnd]:
                endRange = nums[windowEnd]

            else:
                if endRange == None:
                    result.append(str(startRange))
                else:
                    result.append("" + str(startRange) + "->" + str(endRange))

                startRange = nums[windowEnd]
                endRange = None

            windowStart += 1
            windowEnd += 1

        if endRange != None:
            result.append("" + str(startRange) + "->" + str(endRange))
        else:
            result.append(str(nums[windowEnd-1]))

        return result
