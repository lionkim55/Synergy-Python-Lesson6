a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print("Четные числа на отрезке:")

for i in range(a, b + 1):
    
    if i % 2 == 0:
        
        print(i, end=" ")