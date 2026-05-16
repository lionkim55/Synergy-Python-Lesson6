n = int(input("Сколько чисел будете вводить: "))
count = 0

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    
    if number == 0:
        count += 1
        
        
print("Количество нулей:",count)