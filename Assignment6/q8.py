x = input("Insert the number separated by comma: ")
list_x = x.split(",")
list_x_num = list(map(int, list_x))

sorted_x = sorted(list_x_num)

print([sorted_x[0], sorted_x[-1]])