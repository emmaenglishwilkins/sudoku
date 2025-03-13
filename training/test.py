test_board, true_solution = generate_sudoku()
test_input = np.array(test_board).reshape(1, 9, 9, 1) / 9.0

predicted = model.predict(test_input).reshape(9, 9) * 9
predicted_solution = np.round(predicted).astype(int)

print("Generated Sudoku Board:")
print(np.array(test_board))
print("\nPredicted Solution:")
print(predicted_solution)
print("\nActual Solution:")
print(true_solution)
