with open('input.txt', 'r') as f:
    data = f.readlines()
nums = [int(d.strip()) for d in data]

pairs = zip(nums[:-1], nums[1:])
result = sum(b > a for (a, b) in pairs)
print(result)
