dict_1 = {'One':1, 'Two':2}
dict_2 = {'Two':2, 'Three':3}
dictionary = {**dict_1, **dict_2}
print(dictionary)

list_1 = ["One","Two","Three"]
list_2 = [1,2,3]
dictionary1 = dict(zip(list_1, list_2))