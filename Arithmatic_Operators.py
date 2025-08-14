milk_price = 2.50
bread_price = 3.75
eggs_price = 4.20

milk_qty = 2
bread_qty = 1
eggs_qty = 3

subtotal = (milk_price * milk_qty) + (bread_price * bread_qty) + (eggs_price * eggs_qty)

discount = subtotal * 0.05 

total = subtotal - discount 

num_items = milk_qty + bread_qty + eggs_qty
average_price = total / num_items

remaining_money = 10.00
full_milk_cartens = remaining_money // milk_price
remaining_change = remaining_money % milk_price

principle = 1000
rate = 0.05
years = 3 
final_amount = principle * (1 + rate) ** years

print(f'Subtotal: ${subtotal}')
print(f'Discount: ${discount:.2f}')
print(f'Total: ${total}')
print(f'Average price per item: ${average_price:.2f}')
print(f'With ${remaining_money:.2f}, you can buy {full_milk_cartens} milk cartens')
print(f' You"l have ${remaining_change:.2f} left after buying milk ')
print(f'Investment after {years} years: ${final_amount:.2f}')
num = 10/3
print(f'{num}')