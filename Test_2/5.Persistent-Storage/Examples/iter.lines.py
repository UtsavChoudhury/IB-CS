import pathlib
f = open(pathlib.Path('/Users/jishnu/Computer Science HL/IB-CS/Term_2/5.Persistent-Storage/Examples/data/points.txt'))
for line in f:
    print(line)
f.close()