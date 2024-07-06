from os.path import exists

def keyboardinput(datatype, caption, errorMessage):
    while True:
        try:
            value = datatype(input(caption))
            return value
        except ValueError:
            print(errorMessage)

def editproduct(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        
        if len(lines) <= 1:
            print("No products to edit.")
            return

        print("Products available for editing:")
        for index, line in enumerate(lines[1:], start=1):  # Skip header
            product, quantity, price = line.strip().split(" | ")
            print(f"{index}: {product} | {quantity} | {price}")
        
        product_index = keyboardinput(int, "Enter the product number to edit: ", "Invalid input, please enter an integer.")
        
        if 1 <= product_index < len(lines):
            product, quantity, price = lines[product_index].strip().split(" | ")
            print(f"Editing {product}")
            new_quantity = keyboardinput(int, "Enter new quantity: ", "Quantity must be an integer.")
            new_price = keyboardinput(float, "Enter new price: ", "Price must be a float.")
            lines[product_index] = f"{product} | {new_quantity} | {new_price}\n"

            with open(filename, "wt") as filehandler:
                filehandler.writelines(lines)
        else:
            print("Invalid product number.")
    
    except Exception as e:
        print("Something went wrong:", e)

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("\nMenu:")
        print("0 -- Exit")
        print("1 -- List")
        print("2 -- Add")
        print("3 -- Edit")

        choice = keyboardinput(int, 'Choice [0,1,2,3]: ', "Choice must be an integer")
        
        if choice == 0:
            print('Thank you for using our system')
            
        elif choice == 1:
            printProduct(filename)
        
        elif choice == 2:
            addProduct(filename)

        elif choice == 3:
            editproduct(filename)

def createFile(filename):
    if not exists(filename):
        try:
            with open(filename, "xt") as filehandler:
                createTitle(filename)
        except Exception as e:
            print("Something went wrong when we created the file:", e)

def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product | Quantity | Price\n")
    except Exception as e:
        print("Something went wrong when we created the file:", e)

def addProduct(filename):
    try:
        product = keyboardinput(str, "Product: ", "Product must be a string")
        quantity = keyboardinput(int, "Quantity: ", "Quantity must be an integer")
        price = keyboardinput(float, "Price: ", "Price must be a float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"{product} | {quantity} | {price}\n")
    except Exception as e:
        print("Something went wrong when appending the product:", e)

def printProduct(filename):
    try:
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        
        if len(lines) <= 1:
            print("No products available.")
            return
        
        # Print the header once
        header = f"{'Product':40}{'Quantity':20}{'Price':20}"
        print(header)
        print("=" * 80)

        for line in lines[1:]:  # Skip the header line
            product, quantity, price = line.strip().split(" | ")
            print(f"{product:40}{quantity:>20}{price:>20.2f}")
    
    except Exception as e:
        print("Something went wrong when printing the product:", e)

# Initialize the file and run the menu
filename = "fruit.txt"
createFile(filename)
doMenu(filename)

