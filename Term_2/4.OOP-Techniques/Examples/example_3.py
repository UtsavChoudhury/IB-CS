class Parent:
    def __str__(self):
        return 'parent'

class Child(Parent):
    def __str__(self):
        return super().__str__() + ' & child'

p = Parent() # superclass object
c = Child() # subclass object
print(p) # call __str__()
print(c)

