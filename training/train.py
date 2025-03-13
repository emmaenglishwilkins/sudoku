model.fit(X, y, epochs=10, batch_size=64, validation_split=0.1)
model.save("sudoku_solver.h5")
