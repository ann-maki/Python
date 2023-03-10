number = int(input("Введите трехзначное число: "))
sum = 0
count = 3

while count > 0:
    x = number % 10
    number = number//10
    sum += x
    count -= 1

print("Сумма цифр равна: ", sum)