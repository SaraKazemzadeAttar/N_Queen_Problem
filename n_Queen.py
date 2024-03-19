import pygame
import sys

# In the N-Queens problem, each number in the permutation represents the column position of a queen on a chessboard, and the index of the number represents the row position of the queen.
def generate_permutations(sequence): 
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        for i in range(len(sequence)):
            elem = sequence[i]
            rest = sequence[:i] + sequence[i+1:] 
            for perm in generate_permutations(rest): 
                permutations.append([elem] + perm)
        return permutations 
        # example :[0, 1, 2, 3]
        # elem = 0 and rest = [1, 2, 3].It recursively calls itself with [1, 2, 3] and generates [[1, 2, 3], [1, 3, 2]]. Then It adds 0 to the beginning of each permutation: [[0, 1, 2, 3], [0, 1, 3, 2]].
        # then moves to next element , elem = 1 and rest = [0,2,3] , then repeates the process and elem to all permitations of rest 


def is_valid_permutation(perm): 
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if abs(i - j) == abs(perm[i] - perm[j]): # i & j are rows and perm[i],perm[j] are coloumns , This part checks conflicts
                return False
    return True

def solve_n_queens(n):
    permutations = generate_permutations(list(range(n)))
    solutions = []
    for perm in permutations:
        if is_valid_permutation(perm):
            solutions.append(perm)
    return solutions

def get_input():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    font = pygame.font.Font(None, 32)
    input_value = ""
    input_rect = pygame.Rect(145, 170, 200, 50)
    color_inactive = pygame.Color((255, 206, 158))
    color_active = pygame.Color((209, 139, 71))
    color = color_inactive
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return int(input_value)
                    elif event.key == pygame.K_BACKSPACE:
                        input_value = input_value[:-1]
                    else:
                        input_value += event.unicode
        screen.fill((255, 206, 158))
        pygame.draw.rect(screen, color, input_rect)

        text_surface = font.render("Please Type Number Of Queens", True, pygame.Color('black'))
        screen.blit(text_surface, (75, 137))

        txt_surface = font.render(input_value, True, pygame.Color('white'))
        screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)


        text_surface_below = font.render("Press Enter Then Press Space To Continue", True, pygame.Color('black'))
        screen.blit(text_surface_below, (25, 235))  

        # Add text
        text_surface_explain = font.render("There is no solution for 2 or 3 queens", True, pygame.Color('White'))
        screen.blit(text_surface_explain, (55, 290)) 
        pygame.display.flip()



n = get_input()
solutions = solve_n_queens(n)
print(solutions) 

pygame.init()

SQUARE_SIZE = 50  # The size of a square on the chessboard
BOARD_COLOR_1 = (255, 206, 158)  # Light square color
BOARD_COLOR_2 = (209, 139, 71)   # Dark square color
QUEEN_COLOR = (0, 0, 0)        # Color for the queen

board_size = SQUARE_SIZE * n
screen = pygame.display.set_mode((board_size, board_size))
pygame.display.set_caption('N-Queens Solution')


queen_symbol = "Q"
queen_font = pygame.font.SysFont(None, SQUARE_SIZE)

def draw_board():
    screen.fill(BOARD_COLOR_1)
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 1:
                square = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, BOARD_COLOR_2, square)

def draw_queens(solution):
    for row, col in enumerate(solution):
        queen_text = queen_font.render(queen_symbol, True, QUEEN_COLOR)
        screen.blit(queen_text, (col * SQUARE_SIZE, row * SQUARE_SIZE))

running = True
current_solution = 0  # Index of the current solution
draw_board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Check if a key is pressed
            if event.key == pygame.K_SPACE:
                draw_board()
                draw_queens(solutions[current_solution])  # Display the current solution
                pygame.display.flip()
                current_solution = (current_solution + 1) % len(solutions)  # Move to the next solution
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
sys.exit()

