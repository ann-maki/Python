import random
n = int(input("Введите количество элементов массива: "))
lst = [random.randrange(100) for _ in range(n)]
print(lst)
x = int(input("К какому приближаемся: "))

lst_2 = []
for i in lst:
    lst_2.append(abs(i-x))
print(f"Самый близкий элемент равен {lst[lst_2.index(min(lst_2))]}")