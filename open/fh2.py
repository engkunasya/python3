def keyboardInput(type, prompt, error_message):
    while True:
        try:
            return type(input(prompt))
        except ValueError:
            print(error_message)

def createFile(filename):
    try:
        with open(filename, "xt") as filehandler:
            pass
    except FileExistsError:
        pass

def createTitle(filename):
    filehandler = open(filename, "wt")
    try:
        filehandler.write("Product|Quantity|Price\n")
    except Exception as e:
        print("Something went wrong when we create the header:", e)
    finally:
        filehandler.close()

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ", "Price must be Float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"{product}|{quantity}|{price}\n")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

filename = "fruits.txt"
createFile(filename)
createTitle(filename)
addProduct(filename)