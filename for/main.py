from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

def shortest_names(lst):
    shortest = len(min(lst, key=len))
    shortest_names_list = []
    for i in lst:
        if len(i) == shortest:
            shortest_names_list += [i]
    return shortest_names_list
        
def most_vowels(lst):    
    #sorted_lst = sorted(lst, key=lambda word: sum(ch in 'aeiou' for ch in word), reverse=True)
    max_count = 0
    top3 = []
    most_vowels_for_now = ''
    for x in range(3):        
        max_count = 0
        for i in lst:
            count = 0
            for ch in i:
                if ch in 'aeiouAEIOU':
                    count += 1                    
                if count > max_count:
                    most_vowels_for_now = i
                    max_count = count        
        if most_vowels_for_now in lst:
            lst.remove(most_vowels_for_now)
            top3 += [most_vowels_for_now]            
    return top3


def alphabet_set(lst):
    countries_lower_case = [x.lower() for x in lst]
    sorted_lst = sorted(countries_lower_case, key=len, reverse=True)
    letters = "abcdefghijklmnopqrstuvwxyz"
    alphabet = []
    alphabet2 = []
    alphabet_removed = []
    for ch in letters:
        alphabet += [ch]
        alphabet2 += [ch]
        alphabet_removed += [ch]
        
    country_list = []
    country_list_temp = []


    for x in range(10):
        max_count = 0
        country_list_temp = []

        for i in sorted_lst:
            count = 0
            alphabet2 = alphabet_removed[:]
            for ch in i:            
                if ch in alphabet2:
                    alphabet2.remove(ch)
                    count += 1                
            if count > max_count:
                max_count = count
                country_list_temp = [i]             
        
        if not country_list_temp:
            return f'Failed: country list has no new characters remaining. Ended up using {len(country_list)} countries, and still have {len(alphabet_removed)} letters remaining.\n These are the countries used: {country_list} \n These are the remaining letters {alphabet_removed}\n'
            

        print('The alphabet will loose', max_count, 'letter(s), thanks to', country_list_temp[0])
        
        for i in country_list_temp:
            for ch in i:            
                if ch in alphabet_removed:
                    alphabet_removed.remove(ch)
                    if i not in country_list:
                        country_list += [i] 
                    if i in sorted_lst:
                        sorted_lst.remove(i)
                    if not alphabet_removed:
                        return f'\nDone! The alphabet has no more letters remaining. You used the following {len(country_list)} countries to achieve this: {country_list}'                
            alphabet2 = alphabet_removed[:]

        print('The alphabet has the following remaining letters, after iteration ', x, ': ', alphabet2,'\n')
    return f'Failed: reached the end by using {len(country_list)} countries, and still have {len(alphabet_removed)} letters remaining. These are the countries used: {country_list}'


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """

    print(shortest_names(countries))
    print(most_vowels(countries))    
    print(alphabet_set(countries))
    