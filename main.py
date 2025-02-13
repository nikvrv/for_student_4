
def one():
    print("hello")

def hello():
    one()
    print("hello world")
    two()

def two():
    print("world")

if __name__ == "__main__":
    hello()