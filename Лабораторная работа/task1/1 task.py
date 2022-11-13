import pprint

# TODO решить с помощью list comprehension и распечатать его
list_ = []
keys = ['bin', ' dec', 'hex', 'oct']
dict_ = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i), } for i in range(16)]
list_.append(dict_)
pprint.pprint(dict_)
