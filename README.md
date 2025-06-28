# saki_alert
## これは何？
咲季ちゃんが特定の時間になると画面にアラート表示で発言をしてくれるスクリプトです。
咲季ちゃんの可愛い画像付きで、時間帯に応じたメッセージが表示されます。
## 説明
- 朝の4時(〜5時)
  - 「朝の4時よ！これから走りに出るんでしょ？」
    - トップを目指すアイドルの朝は早い
    - <img src=https://github.com/user-attachments/assets/f0d529f5-a3a6-49dd-976f-ebbffd033933 width="400">
- 夜の8時(〜9時)
  - 「じゃ、おやすみっ！ ぐー。」
    - 寝る子は育つ
    - <img src=https://github.com/user-attachments/assets/ec4ca2b6-ecfd-4f31-bac0-7f65d528452f width="400">
- 夜の9時〜翌朝4時
  - 「……すぅ……」
    - 寝ています。鼻つまんでも起きません、寝かせておいてあげましょう
    - <img src=https://github.com/user-attachments/assets/764397db-ca26-4057-acac-3df4dc0091d0 width="400">
    - <img src=https://github.com/user-attachments/assets/3bf3f46c-88f8-457a-84c6-24f673d70ae0 width="400">
    - <img src=https://github.com/user-attachments/assets/ecdb6fa6-6350-4268-932d-102d97e71b0e width="400">
- 日曜日の昼の12時(〜13時)
  - 「昼寝をするわっ！」
    - 休む時も全力
    - <img src=https://github.com/user-attachments/assets/e09e3022-e982-495e-ae35-7e6a4f77217d width="300"> 
- それ以外の時間
  - 「お姉ちゃんに任せなさいっ！」
    - お姉ちゃんに任せれば全て安心(？)
    - <img src=https://github.com/user-attachments/assets/8c9dc9ce-58f7-4e1c-b5ae-f6027ef1cf4a width="300">
## 使い方
### 前提条件
必要なライブラリをインストールしてください：

1. **tkinter**（通常Pythonに標準で含まれています）：
```bash
# macOSでtkinterサポートが必要な場合
$ brew install python-tk
```

2. **必要なPythonライブラリ**：
```bash
$ python3 -m venv new_venv
$ source new_venv/bin/activate
$ pip install schedule Pillow requests
```

### 手動で動作確認したい時
```bash
$ source new_venv/bin/activate
$ python3 saki_alert.py
```
時間帯に応じた咲季ちゃんの画像付きアラートダイアログが表示されます。

### 自動でアラート表示させる時（推奨）
```bash
# バックグラウンドで常駐実行
$ source new_venv/bin/activate
$ python3 saki_alert.py &
```

**自動実行スケジュール：**
- 毎日 朝4時
- 毎日 夜8時  
- 毎日 夜9時
- 日曜日 昼12時

プログラムを停止したい場合は `Ctrl+C` を押すか、プロセスを終了してください。

## 新機能
- **画像付きアラート**: 時間帯に応じた咲季ちゃんの画像が表示されます
- **改善されたUI**: 見やすいレイアウトと色使いでアラートを表示
- **アスペクト比保持**: 画像が適切なサイズで表示されます
- **インターネット画像対応**: GitHubなどのURLから画像を直接取得して表示

### 旧方式（cron）での定期実行
```bash
# crontabでスケジュールを設定する場合
$ sudo crontab -e 

# 例：毎日18時19分にログ出力
19 18 * * * /usr/local/bin/python3 /Users/<ユーザ名>/PycharmProjects/saki_alert/saki_alert.py >> /Users/<ユーザ名>/PycharmProjects/saki_alert/output.log 2>&1
```
