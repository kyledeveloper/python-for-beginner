class LessThanZeroError(Exception):
    def __init__(self,value) -> None:
        self.value = value

def add( *args):
    print(args)
    sum = 0
    for index in range(len(args)):
        if args[index] < 0 :
            raise LessThanZeroError(f'less than zero')
        sum += args[index]
        print(sum)

try:
    add(1, 2, 3, 44,-1)


except TypeError as expt:
    print(expt)
    print("type_error")
except LessThanZeroError as expt:
    print(expt)
    print("cme")
except:
    print("error occured")