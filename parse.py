from pprint import pprint
dict = {'alphabet': set('a b c d e f g'.split()),
        'numbers' :set('0 1 2 3 4 5 6 7 8 9'.split())
        }
print(dict.items())
print(dict.values())

word = 'football'
print({letter : word.count(letter) for letter in word })
print(dict)
pprint(dict)