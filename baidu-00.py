n, m, k = map(int, input().split())

if(n < m):
    print(n - k // m)
else:
    print(m - k // n)
