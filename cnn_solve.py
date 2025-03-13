import tensorflow as tf
import numpy as np

# Load a trained Sudoku CNN model
model = tf.keras.models.load_model("best_weights.hdf5")

def predict_sudoku(board):
    board = np.array(board).reshape(1, 9, 9, 1) / 9.0  # Normalize and reshape
    predicted = model.predict(board).reshape(9, 9) * 9  # Rescale
    return np.round(predicted).astype(int)

# sudoku_board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

board = Board()
board.generate_board()
board.remove_tiles(80)

solution = predict_sudoku(sudoku_board)
print(solution)
