
nums = list(map(int, input(">> ").split())); n = len(nums)
if n == 1: print(nums[0])
else: print(*[nums[(i - 1) % n] + nums[(i + 1) % n] for i, num in enumerate(nums)])
