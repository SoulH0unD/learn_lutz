def Tracer(classname, supers, classdict):
    aClass = type(classname, supers, classdict)

    class Wrapper:
        def __init__(self, *args, **kargs):
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace:', attrname)
            return getattr(self.wrapped, attrname)
        
    return Wrapper

class Person(metaclass = Tracer):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
    
bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())