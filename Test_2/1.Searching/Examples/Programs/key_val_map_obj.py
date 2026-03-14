class Reservation:
    def __init__(self, name, room):
        self.name = name
        self.room = room


reservations = [Reservation('Ville', 101), Reservation('Maija', 103)]

def seq_search_rooms(name, reservations):
    index = 0

    while index < len(names):
        r = reservations[index]
        if r.name == name:
            return r.room
        index += 1

    return -1

names = ['Ville', 'Maija']
rooms = [101, 103]
print(seq_search_rooms('Maija', reservations))
print(seq_search_rooms('Farid', reservations))

