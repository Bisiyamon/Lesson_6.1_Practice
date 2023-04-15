#Найдите сумму цифр трехзначного числа

a = int(input("Input a triple digits  "))
print(f"Sum of numbers in digit = {a%10+a%100//10+a//100}")