#Требуется написать программу, которая проверяет счастливость билета

a = input("Введите номер билета: ")
if int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5]):
    print("Счастливый билет")
else:
    print("Не повезло")

""" for i in a:
    if sum(a[:3]) == sum(a[3:]):
        print("Счастливый билет")
    else:
        print("Не повезло") 
           Как тут преобразовать в число, куда ставить int?"""

