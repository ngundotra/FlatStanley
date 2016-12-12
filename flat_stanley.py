
# coding: utf-8

# In[1]:

# Created by ngundotra 12-11-16
# if you are running python 3.x, comment out the following line
from __future__ import print_function
from random import shuffle

def get_best_name_in_history(name, male=False):
    '''
    This function takes an all *lower case* name and churns out lots of permutations of the name,
    paired with a few superlatives.
    
    Total # of printed names = len(name) * len(superlatives).
    
    This code is meant to be dense and confusing! Please send your questions to noah@gundotra.org so
    he can explain.
    '''
    gender = "female"
    if male:
        gender = "male"
        
    superlatives = ["Best", "Most Amazing", "Greatest", "Strongest", "Sexiest", "Worthiest", "Most Blesséd", 
                    "Most Admired", "Best Dressed", "Uniquest", "Smartest", "Most Mexican", "Most Indian", "Nerdiest",
                   "Craziest", "Most Desired", "Most Seductive", "Trillest", "Dankest", "Most Memest", "Most Kermit",
                   "One and Only", "Prophesized", "Most Deadly", "Best Looking", "Best Smelling"]
    
    print("Top %d names for %s warriors in every culture ever across the globe over all of human history:" 
          % (len(name)*len(superlatives), gender))

    # There are 26 superlatives

    for i in range(len(name)):
        shuffle(superlatives)
        for adj in superlatives:
            print("The " + adj, end=' ')
            for letter in name:
                if letter == name[i]:
                    letter = chr(ord(letter) - 32)
                print(letter, end='')
            print()
    # python uses indentation instead of bracketing to denote blocks of code
    # so this function declaration ends after this line

get_best_name_in_history("noah", True)

friends = ['Noah', 'Elina']
for i, name in enumerate(friends):
    if i > 0:
        print ("{name} is awesome".format(iteration=i, name=name))
    else:
        print ("{name} sucks a lot".format(iteration=i, name=name))

