def dice_throw(num_dice, num_sides, target):

    dp = [[0]*(target+1) for _ in range(num_dice+1)]

    dp[0][0] = 1

    for d in range(1, num_dice+1):

        for t in range(1, target+1):

            for face in range(1, num_sides+1):

                if t-face >= 0:
                    dp[d][t] += dp[d-1][t-face]

    return dp[num_dice][target]


print("Ways =", dice_throw(2, 6, 7))
print("Ways =", dice_throw(3, 4, 10))