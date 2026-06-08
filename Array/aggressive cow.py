def canPlace(stalls, cows, mid):

    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):

        if stalls[i] - last >= mid:
            count += 1
            last = stalls[i]

        if count == cows:
            return True

    return False


t = int(input())

for _ in range(t):

    n, c = map(int, input().split())

    stalls = []

    for _ in range(n):
        stalls.append(int(input()))

    stalls.sort()

    low = 1
    high = stalls[-1] - stalls[0]

    ans = 0

    while low <= high:

        mid = (low + high) // 2

        if canPlace(stalls, c, mid):
            ans = mid
            low = mid + 1      # try bigger distance
        else:
            high = mid - 1     # reduce distance

    print(ans)