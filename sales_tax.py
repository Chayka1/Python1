# Налоr с продаж 
# Напишите программу, которая попросит пользователя ввести величину покупки. Затем программа должна 
# вычислить федеральный и региональный налог с про­ даж. Допустим, что федеральный налог с продаж составляет 5%, 
# а региональный - 2.5%. Программа должна показать сумму покупки, федеральный налог с продаж, региональный налог с продаж, 
# общий налог с продаж и общую сумму продажи (т. е. сумму покупки и общего налога с продаж).

price = int(input('Введите сумма покупки: '))
federal_tax = price * 0.05
regoinal_tax = price * 0.025
final_price = price + federal_tax + regoinal_tax

print('Сумма покупки: ' + str(price) + '$\n'
      'Федеральный налог с продаж: ' + str(federal_tax) + '$\n'
      'Региональный налог с продаж: ' + str(regoinal_tax) + '$\n'
      'Общий налог с продаж: ' + str(federal_tax + regoinal_tax) + '$\n'
      'Общая сумма продажи: ' + str(final_price) + '$')