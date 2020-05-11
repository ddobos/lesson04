import random

"""
    genereaza un masiv de lungimea indicata, siil complecteaza cu valori random
    
    length - lungimea masivului
"""


def generateIntArray(length):
    return {int(random.random() * i * 10) for i in range(length)}


"""
    creeaza un dictionar cu keile keyz si ii seteaza valorile din values
"""


def setDict(keyz, values):
    d = dict.fromkeys(keyz)
    if len(values) > 0:
        for i in range(len(values)):
            d[keyz[i]] = values[i]
    return d


d = setDict(['a', 'b'], [10, 25])
print(d)


"""
    returneaza un string inversat
"""


def reverceString(str):
    return (str[::-1])


"""
    returneaza lungimea stringului :)
"""


def lengthString(str):
    len = 0
    for i in str:
        len += 1
    return len


print(reverceString('La'))
print(lengthString('La'))
