def fourSum(nums,target):
        L = []
        for a in range(len(nums) - 3):
            for b in range(a + 1,len(nums) -2):
                for c in range(b + 1,len(nums) -1):
                    for d in range(c + 1,len(nums)):
                        if(nums[a] + nums[b] + nums[c] + nums[d] == target):
                            if([nums[a],nums[b],nums[c],nums[d]] not in L):
                                L.append([nums[a],nums[b],nums[c],nums[d]])
        return L
print(fourSum([-5,5,4,-3,0,0,4,-2],8))