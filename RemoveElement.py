nums = input("Enter a list").split(",")
val = input("Enter Integer : ")
index = 0
while index < len(nums):
    if nums[index] == val:
        nums.pop(index)
    else:
        index += 1
print(index)
print(nums)
