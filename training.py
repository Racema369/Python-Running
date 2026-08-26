class Number:
    def input(self):
        self.a=int(input("Enter first number: "))
        self.b=int(input("Enter second number: "))
        
class Calculator:
    def sum(self,object):
        sum=object.a + object.b
        return sum

number=Number()
number.input()
calculator=Calculator()
print(calculator.sum(number))