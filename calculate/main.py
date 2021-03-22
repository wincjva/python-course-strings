# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
sum_one_each = broccoli + leek + potato + brussel_sprout

# print('sum one each:', sum_one_each)
# 
# groceries = [broccoli,leek,potato,brussel_sprout]
# avg_price = sum(groceries) / len(groceries)
# print('average price: ', avg_price)

avg_price = sum_one_each / 4

num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

# num_groceries = [num_broccolis,num_leeks,num_potatoes,num_brussel_sprouts]

# import numpy as np
# a = np.array([broccoli,leek,potato,brussel_sprout])
# b = np.array([num_broccolis,num_leeks,num_potatoes,num_brussel_sprouts])
# individual_prices = a * b
# sum_total = sum(individual_prices)

# print('sum total: ', sum_total)

sum_total = potato*num_potatoes+broccoli*num_broccolis+leek*num_leeks+brussel_sprout*num_brussel_sprouts

discount_percentage = 30

discounted_sum_total = round((1- discount_percentage/100) * sum_total,2)

print(discounted_sum_total)