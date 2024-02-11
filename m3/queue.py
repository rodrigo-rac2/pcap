class QueueError(LookupError):  # Choose base class for the new exception.
    #
    #  Write code here
    #
    pass


class Queue:
    def __init__(self):
        self.__q = []

    def put(self, elem):
        self.__q.append(elem)

    def get(self):
        elem = self.__q[0]
        try:
            elem = self.__q[0]
            del self.__q[0]
        except IndexError:
            raise QueueError
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
