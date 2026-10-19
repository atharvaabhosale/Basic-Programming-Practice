lower = int(input("Enter Lower Number = "))
upper = int(input("Enter Upper Number = "))

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    order = len(str(num))

    while temp > 0:
        digit = temp % 10
        cube = digit ** order
        sum = sum + cube
        # To get a digit by digit
        temp = temp // 10

    if num == sum:
        print(num)
