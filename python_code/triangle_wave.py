"""
学籍番号_2254838
氏名_山口珠生
"""
# triangle_wave
import numpy as np
"""
フーリエ級数を用いて正弦波による三角波の加算合成することが出来るため、
ChatGPTでは「フーリエ級数を用いた正弦波による三角波の加算合成を行うプログラム作成して。」
と入力し出力されたプログラムから基本周波数と時間軸、高周波数の数を引数として関数に改変し実装。
実装した際にはgenerate_triangle_waveとして関数を作成した。
また、フーリエ級数を用いた正弦波による周期信号の合成として参考にしたウェブサイトは以下のURLのサイトである。
https://vrlab.meijo-u.ac.jp/edu/fourier-series-waveform.html
"""

# 三角波を生成
def generate_triangle_wave(FO, t, N_HARMONICS):
    wave = np.zeros_like(t)  # 初期化
    for n in range(1, N_HARMONICS + 1, 2):  # 奇数高調波を加算（平均値（直流分）がゼロとして考えるためNを奇数のみとして扱う）
        wave += (-1)**((n-1)//2) * (np.sin(2 * np.pi * FO * n * t) / (n**2))
    wave *= (8 / (np.pi**2))  # フーリエ係数で振幅を調整。
    return wave
