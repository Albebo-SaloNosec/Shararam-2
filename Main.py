from random import randint
secret_number = randint(1,10)
n = 3
while n > 0:
    answer = int(input("Введите загаданное число: "))
    if answer == secret_number:
        print("Вы выиграли!")
        break
    elif answer == 666:
        print(secret_number)
    else:
        n -= 1
        print(f"Попытайтесь ещё раз, у вас осталось {n} попыток")
        continue
        print(secret_number)