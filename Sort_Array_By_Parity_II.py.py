class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

      #bad n^2 solution
        odd, even = [], []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        e, o = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1
        return nums

      # 2n solution       
        odd, even = [], []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        e, o = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1
        return nums

      #n solution
        e = 0
        o = 1
        n = len(nums)

        while e < n and o < n:
            if  nums[e] % 2 == 0:
                e += 2
            elif nums[o] % 2 != 0:
                o += 2
            else:
                nums[e],nums[o] = nums[o],nums[e]
                e, o = e+2, o+2

        return nums

      #also n
        lst = [0 for i in range(len(nums))]

        even, odd = 0, 1

        for i in nums:
            if i % 2 == 0:
                lst[even] = i
                even += 2
            else:
                lst[odd] = i
                odd += 2
        return lst
