def seq_search_rooms(name, names, rooms):
    index = 0

    while index < len(names):
        if names[index] == name:
            return rooms[index]
        index += 1

    return -1

names = ['Ville', 'Maija']
rooms = [101, 103]
print(seq_search_rooms('Maija', names, rooms))
print(seq_search_rooms('Farid', names, rooms))

