integers = input()
n, h0, a, c, q = map(int, integers.split(' '))
heights = []
heights.append(h0)
for i in range(1, n):
    heights.append((a * heights[i - 1] + c) % q)

count = 0
for i in range(1, n):
    count += 1
    if heights[i-1] <= heights[i-2]:
        count += 1
        
print(count)