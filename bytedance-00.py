n, d = map(int, input().split())
locas = list(map(int, input().split()))

sum = 0
right = 2
left = 0

while(right < n):
    while(left < right and locas[right] - locas[left] > d):
        left += 1
    if(right - left >= 2):
        num = right - left
        sum += num * (num - 1) // 2
    right += 1

print(sum % 99997867)

# newcoder byte dance
