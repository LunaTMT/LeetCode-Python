nums = [1,2,3,1]
dict_ = {}

for elm in nums:
    status = dict_.get(elm, False)
    if not status:
        dict_[elm] = 1
    else:
        print(False)
print(True)
