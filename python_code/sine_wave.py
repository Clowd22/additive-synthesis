"""
学籍番号_2254838
氏名_山口珠生
"""
# sine_wave.py
import numpy as np
"""

ChatGPTで本課題の条件を理解させた上で「三角関数1つで正弦波を合成するプログラム作成して。」
と入力し出力されたプログラムかラ振幅と高周波数、時間軸、を引数として関数に改変し実装。
実装した際にはgenerate_sine_waveとして関数を作成した。
"""

def generate_sine_wave(A, FO, t):

    # 正弦波を生成
    sine_wave = A * np.sin(2 * np.pi * FO * t)
    return sine_wave
