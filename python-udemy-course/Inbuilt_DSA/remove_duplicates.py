def remove_duplicates(nums):
    # Your code goes here
    new_lst = []
    for num in nums:
        if num not in new_lst:
            new_lst.append(num)
    return new_lst
lst = [1,2,2,3,4,4,5]
print(remove_duplicates(lst))