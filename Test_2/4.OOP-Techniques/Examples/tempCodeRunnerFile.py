class Parent:
    def __str__(self):
        return 'parent'

class Child(Parent):
    def __str__(self):
        return super().__str__() + ' & child'

p = Parent() # superclass object
c = Child() # subclass object. This is an example of overriding by class of reference (subtype polymorphism).
print(p) # call __str__()
print(c)

