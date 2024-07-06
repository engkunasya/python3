dict_data = {'a': 1, 'b': 2, 'c': 3, 1: "a"}

for key, value in dict_data.items():
    if value in dict_data and dict_data[value] == key and key != value: #filtering process
        print(key, value)
        # dict_data[value] == key means if dict_data[1 (as curremt value) ] == key (a) which is coincidentally true 
        # for last tuple even tho we are stil in the first tuple of 'a': 1
        #key != value means filter out perfect number by another default.