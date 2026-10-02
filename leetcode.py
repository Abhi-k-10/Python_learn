nums = [2,7,11,15]
target = 9
for x in nums :
    if target - x in nums :
        print(f"[{nums.index(x)} , {nums.index(target - x)}]")
        break