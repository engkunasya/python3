#Multiple inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card class")

class Atmcard(Card):
    def __init__(self):
        pass
 #   def doSomething(self):
#        print("Inside Atmcard class")


class Creditcard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Creditcard class")

class Debitcard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Debitcard class")

class BankCard(Atmcard, Creditcard, Debitcard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside BankCard class")
        super().doSomething()


#we have created 5 classes
# and in all 5 classes we have doSomething method

#let us create instance of last card

bankcard = BankCard()
bankcard.doSomething()
#now remove doSomething within bank card and replace witjh  super
# print(bankcard)
print(bankcard.doSomething())