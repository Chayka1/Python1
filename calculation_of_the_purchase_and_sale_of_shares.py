# Программа расчета купли-продажи акций 
# В прошлом месяце Джо приобрел немного акций некой ИТ-компании. 
# Вот детали этой покупки:
# число приобретенных акций было 2000;
# при покупке акций Джо заплатил 40.00 долларов за акцию;
# Джо заплатил своему биржевому брокеру комиссию, которая составила 3% от суммы, уплаченной за акции.
# Две недели спустя Джо продал акции. Вот детали продажи:
# количество проданных акций составило 2000;
# он продал акции за 42.75 долларов за акцию;
# он заплатил своему биржевому брокеру комиссию, которая составила 3% от суммы, полученной за акции.
# Напишите программу, которая показывает приведенную ниже информацию:
# 
# сумму денег, уплаченную за акции;
# сумму комиссии, уплаченную брокеру при покупке акций;
# сумму, за которую Джо продал акции;
# сумму комиссии, уплаченную брокеру при продаже акций.
# сумму денег, которая у Джо осталось, когда он продал акции и заплатил своему бро­ керу (оба раза). 
# Если эта сумма- положительная, то Джо получил прибыль. Если же она - отрицательная, то Джо понес убытки.

number_of_shares_acquired = 2000
share_price1 = 40
amount_of_purchased_shares = number_of_shares_acquired * share_price1
purchase_commission1 = amount_of_purchased_shares * 0.03
total_price_buy = amount_of_purchased_shares + purchase_commission1

share_price2 = 42.75
sale_of_shares = number_of_shares_acquired * share_price2
purchase_commission2 = sale_of_shares * 0.03
total_price_sell = sale_of_shares - purchase_commission2

total_price = total_price_sell - purchase_commission1

print('Cумма денег, уплаченная за акции: ' + str(total_price_buy) + '$\n' +
      'Cумма комиссии, уплаченная брокеру при покупке акций: ' + str(purchase_commission1) + '$\n' +
      'Сумма денег, за которую Джо продал акции: ' + str(total_price_sell) + '$\n' +
      'Сумма комиссии, уплаченная брокеру при продаже акций: ' + str(purchase_commission2) + '$\n' +
      'Cумма денег, которая у Джо осталась, когда он продал акции и заплатил своему бро­керу (оба раза): ' + 
      str(total_price) + '$')
