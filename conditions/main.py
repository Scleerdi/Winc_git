# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
	if ((Location_of_the_cows == 'pasture' and Time_of_day == 'night') or Weather == 'rainy' and Location_of_the_cows != 'cowshed' and Slurry_tank):
		return 'take cows to cowshed'
	
	if (Location_of_the_cows == 'cowshed' and Cow_milking_status == True):
		return 'milk cows'
	elif (Location_of_the_cows == 'pasture' and Cow_milking_status == True):
		return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'

	if (Slurry_tank == True and Location_of_the_cows == 'cowshed' and (Weather != 'rainy' or 'neutral')):
		return 'fertilize pasture'
	elif (Location_of_the_cows == 'pasture' and Slurry_tank == 'True' and (Weather != 'sunny' or 'windy')):
		return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'

	if (Grass_status == 'True' and Season == 'spring' and Weather == 'sunny' and Location_of_the_cows != 'pasture'):
		return 'mow grass'
	elif (Grass_status == 'True' and Season == 'spring' and Weather == 'sunny' and Location_of_the_cows == 'pasture'):
		return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
	else:
		return 'wait'
	
#print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))      