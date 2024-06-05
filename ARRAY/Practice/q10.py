# Remove all occurence of given element:-

nums = [0,1,2,2,3,0,4,2]

def remove_occurence(nums, val):
    a = []
    for i in nums:
        if i != val:
            a.append(i)
    return len(a),a

print(remove_occurence(nums,2))
