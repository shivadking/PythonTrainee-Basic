import time
import time

some_integer = 1
some_list = [2]

def some_function(some_arg='default_value'):
    print("I'm from user defined module!" + some_arg)

print("run always code")

if __name__ == '__main__':
    print('code run only when executed as script')
