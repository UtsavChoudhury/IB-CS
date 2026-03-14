lst = []
while (inp := input('Enter a word: ')) != '!':
    lst.append(inp)

print('Entering stage two...' "\n")

while (inp := input('Enter a word: ')) != '!':
    if inp in lst:
        print('hit')

print("\n")
print('Program finished' "\n")

