class Cls:
    def __init__(self):
        self.__foo = 'foo value' # private because two underscores
        self._bar = 'bar value' # protected because one underscore
    def get_foo(self): return self.__foo # accessor
    def set_foo(self, foo): self.__foo = foo # mutator

x = Cls()
try:
    print(x.__foo) # this will not work
except Exception as e:
    print('exception:', e)

# but these will
print(x.get_foo()) # using accessor
x.set_foo('new foo value') # using mutator
print(x._Cls__foo) # circumventing mangling
print(x._bar) # direct access to protected
