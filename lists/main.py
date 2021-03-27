# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(lst):
    return(sorted(lst, key=str.lower))

def won_golden_globe(film):
    golden_globes = ['Jaws','Star Wars: Episode IV – A New Hope',
    'E.T. the Extra-Terrestrial','Memoirs of a Geisha']
    golden_globes_lowercase = [x.lower() for x in golden_globes]
    if film.lower() in golden_globes_lowercase:
        return True
    return False

def remove_toto_albums(lst):
    toto_albums = ['Fahrenheit','The Seventh One',
    'Toto XX (two previously unreleased songs)',
    'Falling in Between (sharing lead vocals on one song)',
    '35th Anniversary – Live in Poland','Toto XIV','Old Is New',
    '40 Tours Around the Sun - Live in Holland']
    return [x for x in lst if x not in toto_albums]

for i in range(20,15,-1):
    print(i)

