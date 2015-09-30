import random, sys, os

def clear(): # reset terminal screen
    if 'ix' in os.name:
        return os.system('clear')
    elif 'nt' in os.name:
        return os.system('cls')
    else:
        print("Compatibility Error")
        sys.exit(0)

def make_grid(n): # make a square grid of n size
    if n <= 1:
        print ("ERROR: grid must be at least 2") # max recursion error if <= 1
        sys.exit(0)

    grid = list()
    start_row = 0

    while len(grid) < n * n:
        for i in range(n):
            position = (start_row, i)
            grid.append(position)
        start_row += 1

    return grid

def get_position(grid): # asign each actor a random position on pre-defined grid.

    player_position = random.choice(grid)
    grue_position = random.choice(grid)
    exit_position = random.choice(grid)

    positions = player_position, grue_position, exit_position
    count = 0

    for i in positions:
        if positions.count(i) > 1:
            count +=1

    if count == 0:
        return positions
    else:
        return get_position(grid)

MAP_SIZE = int(input('SET MAP SIZE: ')) # set grid size
MAP_CELLS = make_grid(MAP_SIZE) # get grid

def get_move(current_positon): # return valid moves based on x, y position
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = current_positon

    if y == 0: MOVES.remove('LEFT')
    if x == 0: MOVES.remove('UP')
    if y == MAP_SIZE: MOVES.remove('RIGHT')
    if x == MAP_SIZE: MOVES.remove('DOWN')

    return MOVES

def move_player(move, position): # move actor and return new x, y position
    x, y = position

    if move == 'LEFT': y -= 1
    if move == 'RIGHT': y += 1
    if move == 'UP': x -= 1
    if move == 'DOWN': x += 1

    return x, y

def main(): # main game loop
    PLAYER, GRUE, EXIT = get_position(MAP_CELLS)
    print('PLAYER {}'.format(PLAYER))
    print('GRUE {}'.format(GRUE))
    print('EXIT {}'.format(EXIT))

    while True:
        VALID_MOVES = get_move(PLAYER)

        clear()
        print("It is pitch black. You are likely to be eaten by a grue.")
        print("You're currently in room {}".format(PLAYER))
        print("You can move {}".format(VALID_MOVES))
        print("Enter QUIT to quit")

        MOVE = input("> ")
        MOVE = MOVE.upper()

        if MOVE == 'QUIT':
            break
        elif MOVE in VALID_MOVES:
            PLAYER = move_player(MOVE, PLAYER)
            if PLAYER == GRUE:
                print('You have been eaten by a Grue.')
                sys.exit(0)
            if PLAYER == EXIT:
                print('You have found the exit!')
                sys.exit(0)

if __name__ == ('__main__'):
    main()
