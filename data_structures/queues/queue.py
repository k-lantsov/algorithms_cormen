def isEmpty(q):
    return len(q) == 0

def enqueue(q, x):
    q.append(x)

def dequeue(q):
    if isEmpty(q):
        print('Queue is empty')
        return None
    return q.pop(0)

queue = []
print('queue =', queue)
enqueue(queue, 2)
print('queue =', queue)
enqueue(queue, 4)
print('queue =', queue)
enqueue(queue, 6)
print('queue =', queue)
print('Queue is empty?', isEmpty(queue))
print('pop elem =', dequeue(queue))
print('pop elem =', dequeue(queue))
print('pop elem =', dequeue(queue))
print('pop elem =', dequeue(queue))
print('Queue is empty?', isEmpty(queue))