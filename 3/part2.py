with open('data.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()

digits = ['0','1','2','3','4','5','6','7','8','9']

def find_star_coordinates(data):
    coordinates = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '*':
                coordinates.append([i,j])
    return coordinates

def find_adjacent_coordinates(coordinates):
    adjacent_coordinates = []
    for coord in coordinates:
        i = coord[0]
        j = coord[1]
        adjacent_coordinates.append([
            [i-1,j-1],
            [i-1,j],
            [i-1,j+1],
            [i,j-1],
            [i,j+1],
            [i+1,j-1],
            [i+1,j],
            [i+1,j+1]
        ])
    return adjacent_coordinates

def find_gears(adjacent_coordinates):
    is_adjacent = False
    number = ''
    gear_index = None
    gear_ratios = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            char = data[i][j]
            if char in digits:
                number += char
                for gear_idx, gear_coords in enumerate(adjacent_coordinates):
                    for coord in gear_coords:
                        if [i,j] == coord:
                            is_adjacent = True
                            gear_index = gear_idx
            if (char not in digits) and number:
                if is_adjacent:
                    if gear_index in gear_ratios:
                        gear_ratios[gear_index] = [gear_ratios[gear_index],number]
                    else:
                        gear_ratios[gear_index] = number
                is_adjacent = False
                number = ''
                gear_index = None
    return gear_ratios

coordinates = find_star_coordinates(data)
adj_coordinates = find_adjacent_coordinates(coordinates)
d = find_gears(adj_coordinates)
gear_ratios = {}
for index, gear in d.items():
    if isinstance(gear, list):
        gear_ratios[index] = gear

total = 0
for nums in gear_ratios.values():
    ratio = 1
    for num in nums:
        ratio *= int(num)
    total += ratio

print(total)