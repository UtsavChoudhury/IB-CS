import random
import pathlib
import pickle

text_file = pathlib.Path('Term_2/5.Persistent-Storage/Homework/data/random.txt')
pickle_file = pathlib.Path('Term_2/5.Persistent-Storage/Homework/data/random.ser')

try:
    with open(text_file, 'r') as f:
        test_text = []
        for line in f:
            for word in line.split():
                test_text.append(int(word))
    print(test_text[:20])
except FileNotFoundError:
    lst = [str(random.randint(0, 1000)) for _ in range(10000)]
    with open(text_file, 'w') as f: # This will create a file.
        f.write(' '.join(lst))

try:
    with open(pickle_file, 'rb') as f: # As one big object
        test_pickle = pickle.load(f)
    print(test_pickle[:20])
except FileNotFoundError:
    with open(text_file, 'r') as f: 
        test_text = []
        for line in f:
            for word in line.split():
                test_text.append(int(word))
    with open(pickle_file, 'wb') as f:
        pickle.dump(test_text, f)


# There might be some other issues if the pickle file is empty.
