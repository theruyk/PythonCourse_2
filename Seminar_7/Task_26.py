def find_divisors(num):
    divisors = []  # Список для хранения делителей

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

number = int(input("Введите число, чтобы найти все его делители: "))
print("Делители числа", number, ":", find_divisors(number))
