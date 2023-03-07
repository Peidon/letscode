n, d = map(int, input().split())
lo_lis = list(map(int, input().split()))

_sum = 0
right = 2
left = 0

while right < n:
    while left < right and lo_lis[right] - lo_lis[left] > d:
        left += 1
    if right - left >= 2:
        num = right - left
        _sum += num * (num - 1) // 2
    right += 1

print(_sum % 99997867)

# byte dance
