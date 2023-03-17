import random
n = int(input("Введите количество элементов массива: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)
x = int(input("Какое число искать: "))
count = 0
for i in lst:
    if i == x:
        count += 1
print(f"Встретилось {count} раз")