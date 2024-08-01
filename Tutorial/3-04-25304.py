price_total = int(input())
num_item = int(input())
price_sum = 0
for i in range(num_item):
    price_each, num_each = input().split()
    price_sum += int(price_each)*int(num_each)
print("Yes" if price_sum == price_total else "No")