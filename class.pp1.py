class string_function:
    def __init__(self, string ):
        self.string = string
    def getString(self):
        self.string=str(input())
    def printString(self):
        print(self.string.upper())

python=string_function
python.getString(python)
python.printString(python) 