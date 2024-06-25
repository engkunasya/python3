# sys.argv give us a list , ehich contains all da CLA
# 0 IS THE NAME OF THE Program itself, aka the filename
# these arguments are separated by space
# all these srguments inside this list are string
# remember, but the arguments for functions is separated by comma
#
import sys

cmdarguments = sys.argv

# print(cmdarguments)

total = 0
for number in cmdarguments[1:]:
    total = total + int(number)
    print(total)