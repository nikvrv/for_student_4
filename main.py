
def one():
    print("hello")

def hello():
    one()
    print("HI")
    two()

def two():
    print("world")

if __name__ == "__main__":
    hello()