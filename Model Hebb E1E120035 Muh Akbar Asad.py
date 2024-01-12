import numpy as np
import os
os.system("cls")

# fungsi aktivasi hard limit
def hard_limit(x):
    result = 1 if x >= 0 else -1
    return result

# inisialisasi bobot
bobot = np.zeros((3, 3), dtype=int)

# input data training
data_training = [
    (np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]]), 1, "X"),
    (np.array([[1, -1, -1], [1, -1, -1], [1, 1, 1]]), -1, "L"),
]

# nilai bobot baru
i = 0
while i < len(data_training):
    x, t, _ = data_training[i]
    bobot += x * t
    i += 1

# input data baru
print("Input pola baru :")
input_baru = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        input_baru[i][j] = int(input(f"Input matrix[{i + 1},{j + 1}] : "))

# menghitung aktivasi dengan hard limit
aktivasi = np.sum(input_baru * bobot)
nilai_Y = hard_limit(aktivasi)
label_huruf = data_training[0][2] if nilai_Y >= 0 else data_training[1][2]

# menampilkan hasil
print("\nNilai bobot : ")
print(bobot)

print("\nPola baru :")
print(input_baru)

print(f"\nNilai aktivasi = {aktivasi}")
print(f"y = {nilai_Y}, dikenali sebagai {label_huruf}")
