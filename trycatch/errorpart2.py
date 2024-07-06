def keyboard(datatype, caption, errorMessage):
    value = None
    IS_INVALID = True
    while IS_INVALID:
        try: 
            value = datatype(input(caption))
            IS_INVALID = False
        except:
                print(errorMessage)
        # else:
        #      IS_INVALID = False
    return value
## try compete with except


def calculate_simple_interest():
    """Calculate the simple interest on a loan.
    """
    principle = keyboard(int, "Principle Amount: ", "This must be integer")
    rate = keyboard(int, "Rate: ", "This must be float")
    period = keyboard(float, "Principle Amount: ", "This must be integer")

    interest = (period * principle* rate) / 100
    print("interest: ", interest)
    print('Payable amount: :', principle + interest)


calculate_simple_interest()