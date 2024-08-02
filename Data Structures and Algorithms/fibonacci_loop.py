num2 = 0
num1 = 1

print(num2)
print(num1)

for fibo in range(18):
    newFibo = num1 + num2
    print(newFibo)
    num2 = num1
    num1 = newFibo