n = int(input())
arr = [[0] * n for _ in range(n)]
dp1 = [[0] * n for _ in range(n)]
dp2 = [[0] * n for _ in range(n)]
path1 = [[False] * n for _ in range(n)]  # 用于记录第一条路径的点

# 读取输入并填充arr
a, b, c = map(int, input().split())
while a != 0 or b != 0:
    arr[a-1][b-1] = c
    a, b, c = map(int, input().split())

# 第一次DP，计算最大路径dp1
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp1[i][j] = arr[i][j]
        elif i == 0:
            dp1[i][j] = dp1[i][j-1] + arr[i][j]
        elif j == 0:
            dp1[i][j] = dp1[i-1][j] + arr[i][j]
        else:
            dp1[i][j] = max(dp1[i-1][j], dp1[i][j-1]) + arr[i][j]

# 记录第一条路径
i, j = n-1, n-1
while i > 0 or j > 0:
    path1[i][j] = True
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif dp1[i-1][j] > dp1[i][j-1]:
        i -= 1
    else:
        j -= 1
path1[0][0] = True  # 起点也要标记

# 第二次DP，计算不重叠的第二条路径dp2
for i in range(n):
    for j in range(n):
        if path1[i][j]:  # 跳过已经走过的点
            dp2[i][j] = 0
        elif i == 0 and j == 0:
            dp2[i][j] = arr[i][j]
        elif i == 0:
            dp2[i][j] = dp2[i][j-1] + arr[i][j]
        elif j == 0:
            dp2[i][j] = dp2[i-1][j] + arr[i][j]
        else:
            dp2[i][j] = max(dp2[i-1][j], dp2[i][j-1]) + arr[i][j]

# 输出两次路径的总采样值
ans = dp1[n-1][n-1] + dp2[n-1][n-1]
print(ans)
