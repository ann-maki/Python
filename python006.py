number = input("Введите номер билета: ")
leftPart = int(number[0]) + int(number[1]) + int(number[2])
rightPart = int(number[3]) + int(number[4]) + int(number[5])
print("Счастливый билет" if leftPart == rightPart else "Несчастливый билет")