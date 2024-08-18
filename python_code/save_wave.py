"""
学籍番号_2254838
氏名_山口珠生
"""
# save_wave
import numpy as np
from scipy.io.wavfile import write

# 波形を保存する関数
def generate_save_wave(filename, wave, fs):
    wave = wave / np.max(np.abs(wave))  # 正規化
    wave = np.int16(wave * 32767)       # 16ビット整数に変換
    write(filename, fs, wave)