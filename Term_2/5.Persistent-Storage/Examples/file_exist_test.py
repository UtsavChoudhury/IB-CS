from os import path
import pathlib

# under directory data, file data.ser
file_path = pathlib.Path('//Users/jishnu/Computer Science HL/IB-CS/Term_2/5.Persistent-Storage/Examples/data/points.ser') # ABSOLUTE PATH
# or
file_path = pathlib.Path('data') / 'data.ser'  # CURRENT WORKING DIRECTORY, THEN THE FILE INSIDE. DOESN'T WORK IN THIS CASE
if file_path.exists():
    print('reading', file_path)
else:
    print('no file', file_path)
