# Generate multiple boards
num_samples = 50000  # Adjust as needed
sudoku_data = [generate_sudoku() for _ in range(num_samples)]

# Save dataset
np.save("sudoku_puzzles.npy", [x[0] for x in sudoku_data])  # Unsolved boards
np.save("sudoku_solutions.npy", [x[1] for x in sudoku_data])  # Solved boards