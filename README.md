# saki_alert
## これは何？
咲季ちゃんが特定の時間になると発言をしてくれるスクリプトです。
## 説明
- 朝の4時(〜5時)
  - 「朝の4時よ！これから走りに出るんでしょ？」
    - トップを目指すアイドルの朝は早い
    - <img src=https://github.com/user-attachments/assets/f0d529f5-a3a6-49dd-976f-ebbffd033933 width="400">
- 夜の8時(〜9時)
  - 「じゃ、おやすみっ！ ぐー。」
    - 寝る子は育つ
    - <img src=https://github.com/user-attachments/assets/ec4ca2b6-ecfd-4f31-bac0-7f65d528452f width="400">
- 夜の8時〜翌朝4時
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
### 手動で動作確認したい時
```
$ python saki_alert.py
```
### 自動で定期実行させる時
```
# crontabでスケジュールを設定する
$ sudo crontab -e 

# スケジュールの書き方
"分 時 日 月 曜日 /Python3のフルパス /実行したいプログラム"

# (例)ログに残す場合
19 18 * * * /usr/local/bin/python3 /Users/<ユーザ名>/PycharmProjects/saki_alert/saki_alert.py >> /Users/<ユーザ名>/PycharmProjects/saki_alert/output.log 2>&1

# ログに残っていれば成功
$ cat output.log
2月24日(月) 18時19分
(咲季): お姉ちゃんに任せなさいっ!
```
