from threading import Timer

def hello():
    print("hello, world")

t = Timer(10.0, hello)
t.start()  # after 10 seconds, "hello, world" will be printed
print("======")
print("Now trying to type some sentences.")
s = input()
print(s)
