print(0)
print(1)
count = 2

def fibonacci(num1,num2):
    global count
    if count <= 19:
        newFibo = num1 + num2
        print(newFibo)
        num2 = num1
        num1 = newFibo
        count += 1
        fibonacci(num1, num2)
    else:
        return
fibonacci(1,0)