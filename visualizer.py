import pygame
from soduku import Board

pygame.init()

# constants 
width = 500
height = 500
cell_size = width / 9 

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200, 200, 200)

font = pygame.font.SysFont('arial', 40)

screen = pygame.display.set_mode((width, height))

def draw_board(board): 
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

board = Board()
board.generate_board()
board.remove_tiles(50)


# if board.solve():
#     print("solvable")
# else:
#     print("too many removed")

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    draw_board(board.board)
    pygame.display.flip()

pygame.quit()