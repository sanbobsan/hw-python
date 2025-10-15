
nums = list(map(int, input(">> ").split())); print(*[i for i in set(nums) if nums.count(i) != 1])
