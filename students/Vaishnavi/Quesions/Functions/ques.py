'''def say(a):
    return a.upper()

print(say("hey"))

def tell(fn):
    g = fn("hello")
    print(g)
tell(say)

def sum(a):
    def add(b):
        return a + b
    return add

v = sum(100) # v = add()

print(v(10))'''

