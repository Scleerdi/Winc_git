from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

def unique_koala_facts(number):
    return_list = []
    i = 0;
    while (i < 1000):
        temp = random_koala_fact()
        if (len(return_list) == number):
            break
        if (temp not in return_list):
            return_list.append(temp)
        i += 1
    return (return_list)

def num_joey_facts():
    joey_facts = []
    i = 10;
    c = 0;
    check = random_koala_fact()
    while (i > 0):
        temp = random_koala_fact()
        if (check == temp):
            i -= 1
        if ("joey" in temp and temp not in joey_facts):
            joey_facts.append(temp)
    return (len(joey_facts))

def koala_weight():
    i = 1
    r = 0
    while (i > 0):
        temp = random_koala_fact()
        if ('kg' in temp):
            while (i < len(temp) - 1):
                if (temp[i] == 'k' and temp[i + 1] == 'g'):
                    hold = temp[i - 2] + temp [i - 1]
                i += 1
            i = 0
    r = int(hold)
    return (r)