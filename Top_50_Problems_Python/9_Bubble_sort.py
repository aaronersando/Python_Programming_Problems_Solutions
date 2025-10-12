nums = list(map(int, input("Enter numbers: ").split()))

def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums

print(bubbleSort(nums))