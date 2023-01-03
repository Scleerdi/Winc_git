# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(names):
	return (sorted(names))

def won_golden_globe(name):
	name = str.lower(name)
	won = ["jaws", "star wars: episode IV - a new hope", "e.t. the extra-terrestrial", "memoirs of a geisha"]
	if name in won:
		return (True)
	return (False)

def remove_toto_albums(names):
	albums = ["Fahrenheit", "The Seventh One", "Toto XX" "Falling in Between", "Toto XIV", "Old Is New"]
	ai = 0
	while (ai < len(names)):
		if (names[ai] in albums):
			names.remove(names[ai])
		else:
			ai += 1
	return (names)
