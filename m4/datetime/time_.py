import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)


##
print(time.ctime()) #now

timestamp = 1572879180
print(time.ctime(timestamp))

##
timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

print(time.gmtime())
print(time.localtime())

##
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

t = time.mktime((1982, 1, 13, 16, 0, 0, 2, 13, 0))
print(t)
print(time.ctime(t))