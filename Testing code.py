class testfile:
    def __init__(self,filename):
        self.filename = filename
    def __str__(self):
        return self.filename

test = testfile("test.txt")
print(test)
test2 = testfile("test.pdf")
print(test2)
test3 = testfile("test.dox")
print(test3)