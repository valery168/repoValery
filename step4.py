pr = int(input('add your proceeds'))

co = int(input('add your costs'))

profit = (pr - co)
profitability = (profit / pr) * 100


if pr <= co:
    print('bad result')
if pr > co:
    print('good result' + str(profitability))
    emp = int(input('add add the number of emplois'))
profit_by_emplois = (profit / emp)
print(str(profit_by_emplois))