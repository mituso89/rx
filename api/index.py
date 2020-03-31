import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

def loger(func):
    # def log_func(*args):
    #     logging.info('runing "{}:'.format(func.__name__, args))
    #     print(func(*args))
    def log_func(*args):
        a = func(*args)
        print(a)
    
    return log_func

def add(a,b):
    return a+ b

log = loger(add)

log(3,4)
