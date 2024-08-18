from flask import Flask, render_template, request, send_file, jsonify
import numpy as np
from io import BytesIO
from sine_wave import generate_sine_wave
from triangle_wave import generate_triangle_wave
from square_wave import generate_square_wave
from sawtooth_wave import generate_sawtooth_wave
from save_wave import generate_save_wave
from scipy.io.wavfile import write

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_wave', methods=['POST'])
def generate_wave():
    # フォームからデータを取得
    freq = float(request.form['frequency'])
    harmonics = int(request.form['harmonics'])
    sample_rate = int(request.form['sample_rate'])
    wave_type = request.form['wave_type']

    # 時間軸を生成
    duration = 3.0
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # 選択された波形に基づいて生成
    if wave_type == 'sine':
        wave_data = generate_sine_wave(1.0, freq, t)
    elif wave_type == 'triangle':
        wave_data = generate_triangle_wave(freq, t, harmonics)
    elif wave_type == 'square':
        wave_data = generate_square_wave(freq, t, harmonics)
    elif wave_type == 'sawtooth':
        wave_data = generate_sawtooth_wave(freq, t, harmonics)
    else:
        return "Invalid wave type", 400

    # メモリ上にWAVファイルを生成
    wav_io = BytesIO()
    wave_data = (wave_data * 32767).astype(np.int16)  # 16bit PCM
    write(wav_io, sample_rate, wave_data)
    wav_io.seek(0)

    # WAVファイルを返す
    return send_file(wav_io, mimetype="audio/wav", as_attachment=False, download_name="generated_wave.wav")

if __name__ == '__main__':
    app.run(debug=True)
