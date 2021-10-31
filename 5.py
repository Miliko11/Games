import random

print("\tДобро пожаловать в игру \"Отгадай число\"")
print("\nЯ загадал число целое от 1 до 15")
number = random.randint(1,15)
popitka = int(input("Ваше предположение: "))
tries = 1

while popitka != number:
    if popitka > number:
        print("Меньше")
    else:
        print("Больше")
    popitka = int(input("Ваше предположение: "))
    tries += 1

    print("\n Да это оно")
    print("\n Вы затратили попыток: ", tries)
