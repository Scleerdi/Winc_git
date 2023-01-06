# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
import json

def create_passport(name, date_of_birth, place_of_birth, height, nationality):

	r_dict = {
		"name": name,
		"date_of_birth": date_of_birth,
		"place_of_birth": place_of_birth,
		"height": height,
		"nationality": nationality
	}
	return (r_dict)


def add_stamp(passport, country):

	stamps = []
	x = passport.keys()
	if ("stamps" not in x):
		passport.update({"stamps": stamps})
	if (country not in stamps):
		stamps.append(country)
		passport.update({"stamps": stamps})
	return (passport)


def add_biometric_data(passport, data_type, data, date):
	if "biometric" not in passport:
		passport["biometric"] = {}
	passport["biometric"].update({data_type: {"date": date, "value": data}})
	return (passport)


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}
omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(json.dumps(omari, indent=4))
