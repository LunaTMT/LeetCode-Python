class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}

        for elm in nums:
            status = dict_.get(elm, False)
            if not status:
                dict_[elm] = 1
            else:
                return True
        return False
