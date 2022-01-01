from itertools import islice


with open('input.txt', 'r') as f:
    data = f.readlines()
nums = [int(d.strip()) for d in data]

sums = [sum(tup) for tup in zip(nums, nums[1:], nums[2:])]
pairs = zip(sums, sums[1:])
result = sum(b > a for (a, b) in pairs)

print(result)
