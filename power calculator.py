n = int(input("Enter a number: "))

for num in range(1, n + 1):
    result = 1

    for i in range(num):
        result = result * num

    print(num, "power", num, "=", result)