from stacks import Stack

def parentheses(string):
    i = 0
    s = Stack()
    while i < len(string):
        if string[i] == "(":
            s.push("(")
        else:
            if s.isEmpty() == True:
                return False
            else:
