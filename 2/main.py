with open('data.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()

digits = ['0','1','2','3','4','5','6','7','8','9']

total = 0

for game in data:
    cube_counts = {'r': 0, 'g': 0, 'b': 0}
    game_started = False
    game_id = ''
    cube_number = ''
    for i in range(len(game)):
        char = game[i]
        match char:
            case char if char in digits and not game_started:
                game_id += char
            case ':':
                game_started = True
            case char if char in digits and game_started:
                cube_number += char
            case 'r'|'g'|'b':
                if int(cube_number) > cube_counts[char]:
                    cube_counts[char] = int(cube_number)
                cube_number = '0'
            case ',' | ';':
                cube_number = ''
    total += (cube_counts['r']*cube_counts['g']*cube_counts['b'])    
    



            
            




print(total)