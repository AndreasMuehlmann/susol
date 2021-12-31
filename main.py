import sys
from colorama import init, Fore

init(autoreset=True)

MAXNUMBER = 9

def read_straights(file):
    straights = []
    for row_count, row in enumerate(file):
        row = row.strip().split()
        assert len(row) <= 9, f'There can only be 9 columms (row: {row_count + 1})'
        if not row:
            continue

        for columm_count, square in enumerate(row):
            assert len(square) <= 1, f'One square can only contain one symbols (row: {row_count + 1}, columm: {columm_count + 1}.'
            assert square.isdigit() or square == 'e',\
                f'A square with one symbol can only contain an "e" or a digit from "1" to "9" (row: {row_count + 1}, columm: {columm_count + 1}).'
            if square.isdigit():
                assert 1 <= int(square) <= 9,\
                    f'Numbers can only be digits from "1" to "9" (row: {row_count + 1}, columm: {columm_count + 1}).'

        straights.append(row)

    assert len(straights) <= 9, f'There can only be 9 rows.'
    return straights

def is_valid(straights):
    for y in range(MAXNUMBER):
        for x in range(MAXNUMBER):
            if  straights[y][x] == 'e':
                continue

            number = int(straights[y][x])

            if  number in give_interferring(straights, x, y):
                return False, x + 1, y + 1
            continue
    return True, -1, -1

def give_numbers_h(straights, static_index, search_range):
    numbers = []
    for changing_index in search_range:
        if straights[static_index][changing_index].isdigit():
            numbers.append(int(straights[static_index][changing_index]))

    return numbers

def give_numbers_v(straights, static_index, search_range):
    numbers = []
    for changing_index in search_range:
        if straights[changing_index][static_index].isdigit():
            numbers.append(int(straights[changing_index][static_index]))

    return numbers

def give_numbers_box(straights, start_x, start_y):
    numbers = set()

    for box in range(1, 4):
        if box >= (start_x + 1) / 3:
            box_start_x = (box - 1) * 3
            break

    for box in range(1, 4):
        if box >= (start_y + 1) / 3:
            box_start_y = (box - 1) * 3
            break 

    assert box_start_y != -1 and box_start_x != -1, 'shit'

    for y in range(box_start_y, box_start_y + 3):
        for x in range(box_start_x, box_start_x + 3):
            if straights[y][x].isdigit() and not (y == start_y and x == start_x):
                numbers.add(int(straights[y][x]))
    return numbers

def give_interferring(straights, x, y):
    numbers = set()

    new_numbers = give_numbers_v(straights, x, range(y + 1, MAXNUMBER, 1))
    numbers.update(new_numbers)

    new_numbers = give_numbers_v(straights, x, range(y - 1, -1, -1))
    numbers.update(new_numbers)

    new_numbers = give_numbers_h(straights, y, range(x + 1, MAXNUMBER, 1))
    numbers.update(new_numbers)

    new_numbers = give_numbers_h(straights, y, range(x - 1, -1, -1))
    numbers.update(new_numbers)

    new_numbers = give_numbers_box(straights, x, y)
    numbers.update(new_numbers)

    return numbers

def give_possible_numbers(interferring_numbers):
    numbers = [number for number in range(1, MAXNUMBER + 1)]
    if interferring_numbers:
        numbers = list(filter(lambda number : (number not in interferring_numbers), numbers))

    return numbers
    

def solve(straights, x , y):
    if y >= MAXNUMBER:
        return straights, True

    if straights[y][x] != 'e':
        if x == 8:
            return solve(straights, 0, y + 1)
        return solve(straights, x + 1, y)
    
    

    for number in give_possible_numbers(give_interferring(straights, x, y)):
        temp = straights[y][x]
        straights[y][x] = str(number)

        if x == 8:
            straights, possible = solve(straights, 0, y  + 1)
            if possible:
                return straights, True
            straights[y][x] = temp

        else:
            straights, possible = solve(straights, x + 1, y)
            if possible:
                return straights, True
            straights[y][x] = temp

    return straights, False 

def give_hints(straights):
    print('"exit" to exit the programm.')
    print('"solution" to see the solution.')
    print('A number from 1 to 9 as koordinates to get the content.')
    print('For example "3 5" shows the content of the square in columm 3 and row 5.')
    while True:
        message = input('Enter a message\n')
        if message == 'exit':
            sys.exit(0)

        elif message == 'solution':
            return

        else:
            message = message.split()
            if len(message) != 2:
                print('There must be two koordinates.')
                continue
            
            elif not message[0].isdigit() and not message[1].isdigit():
                print('Koodinates have to be numbers.')
                continue

            elif not 1 <= int(message[0]) <= 9 and not 1 <= int(message[0]) <= 9:
                print('Koordinates have to be from 1 to 9.')
                continue
            
            else:
                print(f'\nsquare in row: {message[1]} and columm: {message[0]}')
                print(f'\t{straights[int(message[1]) - 1][int(message[0]) - 1]}\n')

def print_sudoku(straights):
        for i_line, line in enumerate(straights):
            if i_line == 0 or i_line == 3 or i_line == 6:
                print(f'{Fore.LIGHTBLACK_EX}-------------------------------------')
            else:
                print('-------------------------------------')


            print(f'{Fore.LIGHTBLACK_EX}|', end='')
            for i_column, square in enumerate(line):
                if i_column == 2 or i_column == 5 or i_column == 8:
                    print(f' {square}{Fore.LIGHTBLACK_EX} |', end='')
                else:
                    print(f' {square} |', end='')
            print() 

        print(f'{Fore.LIGHTBLACK_EX}-------------------------------------')

def print_SUDOKU():
    print(Fore.BLUE + '      +------------------+')
    print(            '      |       SUDOKU     |')
    print(Fore.BLUE + '      +------------------+\n')

def main():
    assert len(sys.argv) <= 3, f'The programm takes one argument, the input file. {len(sys.argv) - 1} where given.'
    with open(sys.argv[1], 'r') as file:
        straights = read_straights(file)

    valid, x, y = is_valid(straights)
    assert valid, f'A number is conflicting with the number in row: {y} and columm: {x}.'

    solved_straights, possible = solve(straights, 0, 0)

    if possible:
        if len(sys.argv) == 3 and sys.argv[2] == '-h':
            give_hints(straights)

        print_SUDOKU()
        print_sudoku(solved_straights)

    else: 
        print('not solveable')

if __name__ == "__main__":
    main()