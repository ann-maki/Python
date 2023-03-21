import random
n = int(input("Введите сколько кустов на грядке: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)

max_harvest = 0
for i in range(n):
    if (i == (n-1)):
        harvest = lst[i-1]+lst[i]+lst[0]
    else:
        harvest = lst[i-1]+lst[i]+lst[i+1]
    if harvest > max_harvest:
        max_harvest = harvest
print(f"Максимальный урожай: {max_harvest}")