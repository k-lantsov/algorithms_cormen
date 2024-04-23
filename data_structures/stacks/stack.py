def isEmpty(s):
    return len(s) == 0

def push(s, x):
    s.append(x)

def pop(s):
    if isEmpty(s):
        print('Stack is empty')
        return None
    return s.pop()

stack = []
print('is empty?', isEmpty(stack))
print('pop elem =', pop(stack))
print(*stack)