import random


def generateIntArray(length):
    return {int(random.random() * i * 10) for i in range(length)}


def setDict(keyz, values):
    d = dict.fromkeys(keyz)
    if len(values)>0:
        for i in range(len(values)):
            d[keyz[i]] = values[i]
    return d


d = setDict(['a', 'b'], [10, 25])
print(d)
