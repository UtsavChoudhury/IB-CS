import pathlib
file_path = pathlib.Path('/Users/jishnu/Computer Science HL/IB-CS/Term_2/5.Persistent-Storage/Examples/data/points.txt')
with open(file_path) as f: # with establishes new context
    for line in f:
        print(line, end='')
# context closes, file closed automatically

# Context -> Special environment for certain rules and resources are applied.
# When we open a file we are creating a context because it is a special environment.
# The manager takes care of all the technical details like closing and opening, etc.
# We create an object file when we do open(file_path) as f.
# This object file is an instance of a class; this class has different methods which take care of details (manager).