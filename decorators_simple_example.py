
def makeromantic(func):
    def wrapper(*args, **kwargs):
        print("love of my life")
        func(*args, **kwargs)
    return wrapper

def makeaggressive(func):
    def wrapper(*args, **kwargs):
        print("Attenion soldier")
        func(*args, **kwargs)
    return wrapper


@makeaggressive
def present(str_sent):
    print(str_sent)

present("hi")



