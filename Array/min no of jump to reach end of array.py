def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):

        # Agar current index tak pahunch hi nahi sakte
        if i > max_reach:
            return False

        # Sabse door reachable index update karo
        max_reach = max(max_reach, i + nums[i])

    return True