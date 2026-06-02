nums = [1,2,3,4,5,6]

index = 0
for i in range (len(nums)):
    if nums[i]> nums[index]:
        index = i

print(index)