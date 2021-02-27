fibonacci_list = [1, 1] #последовательность фибоначчи
sum_of_even_numbers = 0 #сумма всех четных элементов

fib1 = 1
fib2 = 1
fib_sum = 0
#Создаем список с послеедовательностью фибоначчи
while fib2 <= 10000000:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    if fib2 <= 10000000:
        fibonacci_list.append(fib2)

print(fibonacci_list)

#Первая часть задания - вывести кол-во элементов в последовательности 
print(f'Количество элементов последовательности = {len(fibonacci_list)}')

#Вторая и третья часть задания - Посчитать сумму всех четных элементов и Вывести все четные элементы
print('Список четных элементов последовательности:')
for i in range(0, len(fibonacci_list)):
    if fibonacci_list[i] % 2 == 0:
        print(fibonacci_list[i])
        sum_of_even_numbers += fibonacci_list[i]
print(f'Сумма всех четных элементов = {sum_of_even_numbers}')

#Четвертая часть задания - Вычислить предпоследнее число последовательности
print(f'Предпоследнее число последовательности = {fibonacci_list[-2]}')