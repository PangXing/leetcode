# coding:utf-8

class CQueue(object):
    def __init__(self):
        self.stack_add = list()
        self.stack_del = list()

    def appendTail(self, value):
        self.stack_add.append(value)

    def deleteHead(self):
        if len(self.stack_del) == 0:
            for i in range(len(self.stack_add)):
                self.stack_del.append(self.stack_add.pop())
        if len(self.stack_del) == 0:
            return -1
        else:
            return self.stack_del.pop()

if __name__ == '__main__':
    q = CQueue()
    q.appendTail(3)
    print q.deleteHead()
    print q.deleteHead()