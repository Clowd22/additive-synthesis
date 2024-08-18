"""
学籍番号_2254838
氏名_山口珠生
"""
# plot_wave.py
import matplotlib.pyplot as plt
"""
生成された波形が正しいかどうかを確認するためにプロットする関数。
ChatGPTを使用して「波形をプロットするプログラムをpythonで書いて」と入力し、
出力されたプログラムを関数として改変し実装した
"""

# 波形をプロット
def plot_wave(t, wave, title):
    plt.figure(figsize=(10, 4))  # プロットのサイズを設定
    plt.plot(t[:1000], wave[:1000])  # 最初の1000サンプルをプロット
    plt.title(title)  # プロットのタイトルを設定
    plt.xlabel('Time [s]')  # x軸のラベルを設定
    plt.ylabel('Amplitude')  # y軸のラベルを設定
    plt.grid()  # グリッドを表示
    plt.show()  # プロットを表示