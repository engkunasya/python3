# tuple is nothing but a read-only list
#
fruits = ["apple", "orange", "mango", "apple"]
print(fruits.count("apple"))

        # del fruits # can
        # del fruits[0] #cant
#tupple is
    #1. take less space
    #2. faster than list
    #3. immutable


def returnFruits(*fruities):
    # return keyword cant return more than 1 value
    #so python must convert the value to "tuple"
    fnew = ""
    for f in fruits:
        fnew+=f

    

    