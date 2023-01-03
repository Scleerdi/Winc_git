from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

def shortest_names(countries):
    len_hold = len(countries[0])
    return_list = []
    for country in countries:
        if (len(country) < len_hold):
            len_hold = len(country)
    for country in countries:
        if (len(country) == len_hold):
            return_list.append(country)
    return(return_list)

def vowel_count(country):
    c = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letters in country:
        if (letters.lower() in vowels):
            c += 1
    return (c)

def most_vowels(countries):
    return_list = ['', '', '']
    temp = ''
    for country in countries:
        vc = vowel_count(country)
        if (vc > vowel_count(return_list[0])):
            temp = return_list[0]
            return_list[0] = country
            country = temp
        if (vc > vowel_count(return_list[1])):
            temp = return_list[1]
            return_list[1] = country
            country = temp
        if (vc > vowel_count(return_list[2])):
            temp = return_list[2]
            return_list[2] = country
            country = temp
    print(return_list)
    return(return_list)

def alphabet_set(countries):
    return_list = []
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for country in countries:
        for letter in country:
            letter = letter.lower()
            if letter in alphabet_list:
                alphabet_list.remove(letter)
                if country not in return_list:
                    return_list.append(country)
    return(return_list)
                

countries = get_countries()
most_vowels(countries)