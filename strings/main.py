# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

name0 = "Ruud Gullit"
name1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = name0 + ' ' + str(goal_0) + ', ' + name1 + ' ' + str(goal_1)
report = name0 + " scored in the " + str(goal_0) + 'nd minute' + '\n' + name1 + " scored in the " + str(goal_1) + 'th minute'

player = "Hans van Breukelen"
t_len = len(player)
fn_len = player.find(' ')
last_name = player[fn_len:t_len]
last_name_len = t_len - fn_len - 1

name_short = player[0:1] + '.' + last_name
first_name = player[0:fn_len]
chant = first_name + '!' + ' '
i = 1
while (i < fn_len):
	if (i + 1 < fn_len):
		chant += player[0:fn_len] + '!' + ' '
	else:
		chant += player[0:fn_len] + '!'
	i += 1
good_chant = chant[len(chant) - 1] != ' '
print(chant)
# no offence but the subject on this is so unclear especially considering the extremely specific answer you check for
# for instance it does not tell me i need a variable called good_chant and yet without it i cant pass
# I mean in the end i glued it all together but i feel i could have done a much cleaner job, sadly i have to run now because i have to do some stuff