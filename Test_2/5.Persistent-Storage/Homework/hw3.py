import pathlib

s = input('Enter absolute text file path: ')
file_path = pathlib.Path(s)

try:
    with open(file_path, 'r') as f:
        lst = []
        for line in f:
            for word in line.split():
                lst.append(int(word))  # should raise ValueError on invalid
    print(sum(lst)/len(lst)) # division by 0 is possible but EOF prevents 
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print("Invalid data found:", e)
except PermissionError as e:
    print(e)
except EOFError as e:
    print(e)
except Exception as e:
    print(e)
