# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

broccoli = 2
num_broccolis = 5
leek = 2
num_leeks = 2
potato = 3
num_potatoes = 7
brussel_sprout = 7
num_brussel_sprouts = 10
discount_percentage = 30

sum_one_each = broccoli + leek + brussel_sprout + potato
avg_price = sum_one_each / 4
sum_total = (broccoli * num_broccolis) + (leek * num_leeks) + (potato * num_potatoes) + (brussel_sprout * num_brussel_sprouts)
discounted_sum_total = sum_total * ((100 - discount_percentage) / 100)
print(discounted_sum_total)