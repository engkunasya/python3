#byb adding 0b the python starts reading it as one one one @ binary
# instead of hundrend or eleven



# owner_permission = 0b111
# print (owner_permission)


# now owner can read, write and execute
# group can read and execute
#others can exe only

# in data science/ml when u were given categorical data u must convert them to numbers
# which machine can understand like ooooo.
# this things are called "feature engineering"
# gender rep 01 for female and 10 for male

#race rep 1000 for malay and 0100 for chinese
#this bit extraction can be use using bitwise and operator

# mask = 0b000111000
# file_permission = 0b111101001
# print(file_permission & mask)
# product = 0b000101000
# print (product)
# print (bin(file_permission & mask) >> 3)
# # output:
# # 101
# # original product: #000101000
# # now shift it to right 3 times (>> 3) and it be  000000101 
# # 4,5,6 bits extracted ( yang tiga tengah tu)
# # AND OPERATOR IS TO EXTRAXC


# print (file_permission | mask)
# print (bin(file_permission | mask))

# #OR | operqtor is used to do set specific bit to one OR turning ON STUFF.
# # OR OPERATOR COULD NOT SET THING TO ZERO
# # OR operator also use for extracting region of interest like tagging specfic face in IMAGE

# # NOT OR (^) operator IS USE TO SET 0 TO 1 AND VICE VERSA 
# # XOR IS ALWAYS 1 FOR TWO ODD NUMBER
# # used for encryption
# print (file_permission ^ mask)
# print (bin(file_permission ^ mask))

#COMPLEMENT

given_number = 5
print (bin(given_number))  
print (~given_number) #1s compliment
print () 

given_number_six_neg = -6
given_number_six_pos = 6
print(f" This is -6:  {bin(given_number_six_neg)}")
print(f" This is 6:  {bin(given_number_six_pos)}")

given_hex = 0xF

print (f"The hexadecimal for given hex of F: {given_hex}")
print(hex(15))





# multiline string
# x = "hello my name is nash i loove cooking \n"



# x= x + "and eating\n"
# \r \t \n 
#\\ extra escape
# r"dsd"   raw string
# y = """hello my name is nash i loove cooking
# and eating and it is delicious"""


# 0b 0x 0o  