class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

a = int(input('First number: '))
b = int(input('Second number: '))
first = calculator(a, b)
input = int(input('enter the mode of operation \n 1:add 2:sub 3:multi 4:div \n'))
if input == 1:
    print(first.addition())
elif input == 2:
    print(first.subtraction())
elif input == 3:
    print(first.multiplication())
elif input == 4:
    print(first.division())
else:
    print('no operation')