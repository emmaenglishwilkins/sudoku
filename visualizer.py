import pygame
from soduku import Board
import keyboard 
import copy 

pygame.init()

# constants 
width = 500
height = 500
cell_size = width / 9 

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200, 200, 200)
BLUE = (48,197,255, 70)
GREEN = (0, 255, 0)

font = pygame.font.SysFont('arial', 40)

screen = pygame.display.set_mode((width, height))

def draw_board(board, is_solved): 
    if is_solved: 
        screen.fill(GREEN)
    else:
        screen.fill(WHITE)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * cell_size + cell_size / 2, i * cell_size + cell_size / 2))
                screen.blit(text, text_rect)
    
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else: 
            thickness = 1
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), thickness)
        pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), thickness)
    
    # highlight selected cell 
    if selected_cell: 
        transparent_surface = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        transparent_surface.fill(BLUE)
        screen.blit(transparent_surface, (selected_cell[1] * cell_size, selected_cell[0] * cell_size))
        #pygame.draw.rect(screen, BLUE, (selected_cell[1] * cell_size, selected_cell[0] * cell_size, cell_size, cell_size), 5)

board = Board()
board.generate_board()

solution = copy.deepcopy(board)

board.remove_tiles(5)

original = copy.deepcopy(board)

selected_cell = None
running = True
editable = False

def check_is_solved(board, solution):
    return board == solution

while running: 
    for event in pygame.event.get():
        # closing window
        if event.type == pygame.QUIT: 
            running = False
        # selecting cell
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = int(y // cell_size)
            col = int(x // cell_size)
            selected_cell = (row, col)
            if original.board[row][col] == 0: 
                # selected_cell = (row, col)
                print("this cell is editable")
                editable = True
            else: 
                print("this cell is NOT editable")
                editable = False
        # typing number
        elif event.type == pygame.KEYDOWN:
            if editable:
                if keyboard.is_pressed('backspace'):
                    board.board[row][col] = 0
                for i in range(1,10):
                    if keyboard.is_pressed(str(i)):
                        board.board[row][col] = i
                editable = True

    is_solved = check_is_solved(board.board, solution.board)

    draw_board(board.board, is_solved)
    pygame.display.flip()

pygame.quit()