nums = [4,3,2,1]

sorted_position = 0
inner_tracker = 1
while sorted_position < len(nums)-1:
    if nums[sorted_position] > nums[inner_tracker]:
        print (nums[sorted_position], nums[inner_tracker])
    sorted_position+=1
    inner_tracker+=1
