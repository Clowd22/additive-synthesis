"""
学籍番号_2254838
氏名_山口珠生
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from sine_wave import generate_sine_wave
from triangle_wave import generate_triangle_wave
from square_wave import generate_square_wave
from sawtooth_wave import generate_sawtooth_wave
from save_wave import generate_save_wave
from plot_wave import plot_wave
from fourier_verification import verification_wave

# 定数の設定
A = 0.5        # 振幅
FO = 440.0     # 基本周波数 Hz
DURATION = 3.0 # 信号の長さ s
FS = 48000     # サンプリング周波数 Hz
N_HARMONICS = 50 # 高調波の数

# 時間軸を生成
t = np.arange(0, DURATION, 1/FS)

# 正弦波を生成
sine_wave = generate_sine_wave(A, FO, t)

# 三角波を生成
triangle_wave = generate_triangle_wave(FO, t, N_HARMONICS)

# 矩形波を生成
square_wave = generate_square_wave(FO, t, N_HARMONICS)

# のこぎり波を生成
sawtooth_wave = generate_sawtooth_wave(FO,t,N_HARMONICS)


# 各波形をWAVファイルとして保存（ファイル名に波形の種類と高調波の数を含む）
generate_save_wave(f"generated_wave/sine.wav", sine_wave, FS)
generate_save_wave(f"generated_wave/triangle_{N_HARMONICS}.wav", triangle_wave, FS)
generate_save_wave(f"generated_wave/square_{N_HARMONICS}.wav", square_wave, FS)
generate_save_wave(f"generated_wave/sawtooth_{N_HARMONICS}.wav", sawtooth_wave, FS)

# 各波形をプロットして確認
plot_wave(t, sine_wave, "Sine Wave")
plot_wave(t, triangle_wave, "Triangle Wave")
plot_wave(t, square_wave, "Square Wave")
plot_wave(t, sawtooth_wave, "Sawtooth Wave")

#基本周波数の検証
print(f"正弦波の基本周波数: {verification_wave(sine_wave,FS)} Hz")
print(f"三角波の基本周波数: {verification_wave(triangle_wave,FS)} Hz")
print(f"矩形波の基本周波数: {verification_wave(square_wave,FS)} Hz")
print(f"のこぎり波の基本周波数: {verification_wave(sawtooth_wave,FS)} Hz")
