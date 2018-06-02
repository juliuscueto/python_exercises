import numpy as np

class hoge(object):
    def getString(self):
        self.string = input("input a string:")

    def printString(self):
        print(self.string.upper())


if __name__ == "__main__":
    test = hoge()
    test.getString()
    test.printString()
