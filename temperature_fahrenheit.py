# Преобразователь температуры по шкале Цельсия в температуру по шкале Фаренгейта. Напишите программу, которая преобразует показания
# температуры по шкале Цельсия в температуру по шкале Фаренгейта на основе формулы:
# F=~C+32.
# Программа должна попросить пользователя ввести температуру по шкале Цельсия и показать температуру, преобразованную в шкалу Фаренгейта.

t_celsius = float(input('Введите температуру по Цельсию: '))
t_fahrenheit = 9 / 5 * t_celsius + 32
print('Температура по Цельсию: ' + str(t_celsius) + ' грудусов\n'
      'Температура по Фаренгейту: ' + str(t_fahrenheit) + ' градусов')