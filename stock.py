stock_purchase_price = 40
num_shares = 2000
commission_fee_rate = .03
stock_selling_price = 42.75

amount_paid = stock_purchase_price * num_shares
commission_purchase_fee = amount_paid * commission_fee_rate
amount_sold = num_shares * stock_selling_price
commission_sold_fee = amount_sold * commission_fee_rate
amount_profit = amount_sold - amount_paid - commission_purchase_fee - commission_sold_fee

print('Initial stock cost:','$',format(amount_paid))
print('Commission paid for buying:','$',format(commission_purchase_fee))
print('Stock sold return:','$',format(amount_sold))
print('Commission paid for selling:','$',format(commission_sold_fee))
print('Profit:','$',format(amount_profit))
