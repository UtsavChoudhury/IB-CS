def seq_search(target, students, grades):
    index = 0
    while index < len(students):
        if students[index] == target:
            return grades[index]

        index += 1
    return 'QAQ'

students = ['Alissa', 'Ben', 'Charlie', 'Dianna']
grades = ['B', 'D', 'B', 'A']

res = seq_search('Charlie', students, grades)

if res != 'QAQ':
    print(res)

