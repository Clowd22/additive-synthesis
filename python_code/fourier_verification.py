"""
学籍番号_2254838
氏名_山口珠生
"""
import numpy as np
from scipy.fft import fft, fftfreq

"""
作成された波形の基本周波数が440Hzであることを検証するために
ChatGPTに「生成された波形の周波数成分をフーリエ変換による周波数成分の取得とピークの確認をすることで基本周波数を確認するプログラムを作成してください。」
と入力し、出力されたプログラムを対象の波形とサンプリング周波数が引数となるような関数としてプログラムファイルに改変し実装した。
実装した際にはverification_waveとして関数を作成した。
"""
def verification_wave(wave,FS):
    # フーリエ変換を実行
    N = len(wave)
    yf = fft(wave)
    xf = fftfreq(N, 1 / FS)

    # 正の周波数成分のみを取得
    xf = xf[:N//2]
    yf = np.abs(yf[:N//2])
    # ピークの周波数成分を確認し、それが基本周波数に一致するかを表示。
    peak_frequency = xf[np.argmax(yf)]
    return peak_frequency