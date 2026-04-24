def fourSum(nums, target):
        x = sorted(nums)
        res = []
        n = len(x)

        if n < 4:
            return res

        for i in range(n - 3):
            if i > 0 and x[i] == x[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and x[j] == x[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    psum = x[i] + x[j] + x[l] + x[r]

                    if psum == target:
                        res.append([x[i], x[j], x[l], x[r]])

                        l += 1
                        r -= 1

                        while l < r and x[l] == x[l - 1]:
                            l += 1
                        while l < r and x[r] == x[r + 1]:
                            r -= 1

                    elif psum < target:
                        l += 1
                    else:
                        r -= 1

        return res
nums=[-1,2,0,0,-2,1]
target=0
print(fourSum(nums,target))    