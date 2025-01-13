nums = input("Enter List: ").split(",")
if not nums:
    print("Error.....")
index = 1        
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[index] = nums[i]
        index += 1
print(index)