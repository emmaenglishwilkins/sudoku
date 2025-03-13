from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Reshape

model = Sequential([
    Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(9, 9, 1)),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    Conv2D(128, (3, 3), activation='relu', padding='same'),
    Flatten(),
    Dense(81, activation='softmax'),  # 9x9 output
    Reshape((9, 9, 1))  # Reshape back to grid
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
model.summary()
