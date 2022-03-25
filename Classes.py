class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    # Functions within Classes are called Methods.
    # They're written the same way as regular funcions I believe.
    def introduce_self(self):
        print('Hello, my name is ' + self.name)

# If Class has custom constructors defined, this is the cleaner way to write the code:

r1 = Robot('Tom','red',30)
r2 = Robot('Jerry','blue',40)

# OR, if Class is instead using the default constructor __init__():
#
# r1 = Robot()
# r1.name = 'Tom'
# r1.color = 'red'
# r1.weight = 30
# 
# r2 = Robot()
# r2.name = 'Jerry'
# r2.color = 'blue'
# r2.weight = 40
#

r1.introduce_self()
r2.introduce_self()


# https://www.geeksforgeeks.org/__call__-in-python/
# https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call
# https://www.programiz.com/python-programming/property
# https://numba.pydata.org/numba-doc/latest/user/jit.html -- Speeds up code
