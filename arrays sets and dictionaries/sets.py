# sets are an unordered collection of unique elements
# useful when you need to eliminate duplicates for performance

# declare list:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)  # super usefule

unique_chars = set("aaaaaaaaaabbbbbbbbbbbbbbccccccccddddddddddddfffffffff")
print(numbers)
print(unique_numbers)
print(unique_chars)

if "a" in unique_chars:
    print("it's there")

nums1 = {1, 2, 3, 4, 5}
nums2 = {4, 5, 6, 7, 8}

# usefule union
print(nums1 | nums2)
all_nums = list(nums1 | nums2)
print(all_nums)

# usefule intersection
print(nums1 & nums2)

# difference in sets
print(nums1 - nums2)

# symmetric difference
print(nums1 ^ nums2)
