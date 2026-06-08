used = [False] * len(nums)
pairs = []
max_diff = 0

for _ in range(p):

    min_diff = float('inf')
    a = -1
    b = -1

    for i in range(len(nums)):
        if used[i]:
            continue

        for j in range(i + 1, len(nums)):
            if used[j]:
                continue

            diff = abs(nums[i] - nums[j])

            if diff < min_diff:
                min_diff = diff
                a = i
                b = j

    used[a] = True
    used[b] = True

    pairs.append((nums[a], nums[b]))
    max_diff = max(max_diff, min_diff)

print(pairs)
print(max_diff)