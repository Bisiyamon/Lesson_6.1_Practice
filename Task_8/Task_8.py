m = int(input("Введите количество  долек по ширине: "))
n = int(input("Введите количество долек по длине: "))
k = int(input("Введите количество отламываемых долек: "))
if m*n > k:
    if k%m == 0 or k%n == 0:
        print("Можно красиво отломить")
    else:
        print("Не  получится отломить")
else:
    print("Забирай весь шоколад уже")