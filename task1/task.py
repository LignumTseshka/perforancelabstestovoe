while True: 
    try:
        print("Введите длину массива:")
        n = int(input())
        print("Введите интервал:")
        m = int(input())
        break
    except ValueError:
        print("Ошибка. Повторите ввод чисел.")

index = 0
res = ""

arr = [i + 1 for i in range(n)]

while True:
    res += str(arr[index])
    index = (index + m - 1) % n
    if index == 0:
        break

print(res)
