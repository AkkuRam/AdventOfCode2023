import re

red_limit = 12
green_limit = 13
blue_limit = 14

def cube_conundrum():
    file = open('day2/puzzle-2.txt', "r").readlines()
    id_count = 0
    
    for line in file:
        game_id = int(re.search(r'Game (\d+):', line).group(1))
        split_line = line.split(': ')[1].split(';')
        
        valid_game = True
        
        for group in split_line:
            pairs = group.strip().split(',')
            for pair in pairs:
                count, color = pair.strip().split()
                count = int(count)
                if (color == 'red' and count > red_limit) or \
                   (color == 'green' and count > green_limit) or \
                   (color == 'blue' and count > blue_limit):
                    valid_game = False
                    break
            if not valid_game:
                break
        
        if valid_game:
            id_count += game_id
    
    return id_count

print(cube_conundrum())
