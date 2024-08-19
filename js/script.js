document.addEventListener('DOMContentLoaded', () => {
    const closeButton = document.getElementById('closeDescription');
    const descriptionContainer = document.getElementById('descriptionContainer');

    // 説明文を閉じる処理
    closeButton.addEventListener('click', () => {
        descriptionContainer.style.display = 'none';
        showDescriptionButton.style.display = 'block'; // 「説明文を表示」ボタンを表示
    });
});

// ファイルパスを組み立てる関数
function generateFilePath() {
    // 選択されたオプションを取得
    var frequency = document.getElementById("frequency").value;
    var harmonics = document.getElementById("harmonics").value;
    var waveType = document.getElementById("wave_type").value;

    // ファイルパスを組み立て
    var filePath;
    if (waveType === "sine") {
        // 正弦波の場合は高調波を考慮しない
        filePath = `wav/${waveType}_${frequency}.0Hz.wav`;
    } else {
        // その他の波形の場合は通常通り
        filePath = `wav/${waveType}_${harmonics}_${frequency}.0Hz.wav`;
    }

    return filePath;
}

document.getElementById("playButton").addEventListener("click", function () {
    // ファイルパスを生成
    var filePath = generateFilePath();

    // オーディオプレイヤーにファイルを設定
    var audioPlayer = document.getElementById("audioPlayer");
    audioPlayer.src = filePath;
    audioPlayer.play();
});

document.getElementById("downloadButton").addEventListener("click", function() {
    // ファイルパスを生成
    var filePath = generateFilePath();

    // ダウンロードリンクを作成してクリックさせる
    var a = document.createElement("a");
    a.href = filePath;
    a.download = filePath.split('/').pop(); // ファイル名を取得して設定
    document.body.appendChild(a); // 一時的にリンクをドキュメントに追加
    a.click(); // リンクをクリックしてダウンロードを開始
    document.body.removeChild(a); // クリック後にリンクを削除
});
