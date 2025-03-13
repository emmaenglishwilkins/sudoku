import tensorflow as tf
import numpy as np

# Load dataset
X = np.load("sudoku_puzzles.npy")
y = np.load("sudoku_solutions.npy")

# Normalize data (scale between 0 and 1)
X = X / 9.0
y = y / 9.0

# Reshape for CNN (batch, 9, 9, 1)
X = X.reshape(-1, 9, 9, 1)
y = y.reshape(-1, 9, 9, 1)
