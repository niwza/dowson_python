#! python3

netto_price = int(input('Enter raw car price: '))

tax = netto_price * 0.15
dmv_rate = ( netto_price + tax ) * 0.05
sales_tax = 400
shipping_cost = 500
total = netto_price + tax + dmv_rate + sales_tax + shipping_cost

print('Tax amount: ', tax, '\nDMV charge: ', dmv_rate, '\nSales tax: ', sales_tax, \
      '\nShipping costs: ', shipping_cost, '\nTotal: ', total)