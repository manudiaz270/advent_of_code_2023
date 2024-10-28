with open('data.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()

digits = ['0','1','2','3','4','5','6','7','8','9']


def find_symbol_coordinates(data):
    coordinates = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in digits and data[i][j] != '.':
                coordinates.append([i,j])
    return coordinates

def find_adjacent_coordinates(coordinates):
    adjacent_coordinates = []
    for coord in coordinates:
        i = coord[0]
        j = coord[1]
        adjacent_coordinates.append([i-1,j-1])
        adjacent_coordinates.append([i-1,j])
        adjacent_coordinates.append([i-1,j+1])
        adjacent_coordinates.append([i,j-1])
        adjacent_coordinates.append([i,j+1])
        adjacent_coordinates.append([i+1,j-1])
        adjacent_coordinates.append([i+1,j])
        adjacent_coordinates.append([i+1,j+1])
    return adjacent_coordinates



coordinates = find_symbol_coordinates(data)
adj_coordinates = find_adjacent_coordinates(coordinates)
def find_adjacent_numbers(adj_coordinates, data):
    is_adjacent = False
    total = 0
    number = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            char = data[i][j]
            if char in digits:
                number += char
                if [i,j] in adj_coordinates:
                    is_adjacent = True
            if (char not in digits) and number:
                if is_adjacent:
                    total += int(number)
                is_adjacent = False
                number = ''

    return total

print(find_adjacent_numbers(adj_coordinates, data))


