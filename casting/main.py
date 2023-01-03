# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
leek_order = 'leek 4'
print("Leek is " + str(leek_price) + " euro per kilo.")
sum_total = int(leek_order.find(' ')) * leek_price
print(sum_total)

broccoli_costs = 2.34
broccoli_order = 1.6
sum_cost = 2.34 * 1.6
print(str(broccoli_order) + 'kg broccoli costs ' + str(round(sum_cost, 2)) + 'e')