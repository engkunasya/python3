#file handling
#use keyword open

# only two type offiles in the world, binary and txt files

#------CREATE A NEW FILE

from os.path import exists

# try:
#     open("fruits.txt", "xt")
#     mode = " x,r,w,t, xt"

# except FileExistsError:
#     print("File already exist")

def createfile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
       
        except Exception as e:
            print("Something went wrong when wee create the file:", e)

        finally:
            #filehaqndler is an object of instance file class
            #filehandler inhherit many methods like read, write, close
            filehandler.close()

filename = "fruits.txt"
createfile(filename)

content = input("Fruitename: ")
filehandler = open(filename, "w")
