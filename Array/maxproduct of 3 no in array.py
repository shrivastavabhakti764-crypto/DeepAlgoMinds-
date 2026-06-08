max_product = float('-inf')

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            product = nums[i] * nums[j] * nums[k]
            max_product = max(max_product, product)

return max_product


#optimized solution
nums.sort()     
max_product = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
return max_product