
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()

text = input('Please enter the string: ')

for x in text:
    s.push(x)

reversed_str = ''

while not s.is_empty():
    reversed_str = reversed_str + s.pop()

if text == reversed_str:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
