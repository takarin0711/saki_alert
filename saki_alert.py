import datetime
import locale
import tkinter as tk
from tkinter import messagebox
import schedule
import time
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_image_from_url(url, max_width=250, max_height=250):
    """URLから画像を取得してアスペクト比を保持してリサイズ"""
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        
        # アスペクト比を保持してリサイズ
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"画像の読み込みに失敗: {e}")
        return None

def show_custom_alert(root, title, message, image_url=None):
    """カスタムアラートウィンドウを表示"""
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry("350x450")
    window.configure(bg='#f0f8ff')
    window.resizable(False, False)
    
    # ウィンドウを最前面に表示
    window.lift()
    window.attributes('-topmost', True)
    window.grab_set()  # モーダルウィンドウにする
    
    # タイトルラベル
    title_label = tk.Label(window, text="💫 咲季からのメッセージ 💫", 
                          font=('Arial', 14, 'bold'), 
                          bg='#f0f8ff', fg='#4169e1')
    title_label.pack(pady=(15, 5))
    
    # 画像を表示
    if image_url:
        photo = get_image_from_url(image_url, 250, 250)
        if photo:
            # 画像用のフレーム
            img_frame = tk.Frame(window, bg='white', relief='ridge', bd=2)
            img_frame.pack(pady=10, padx=20)
            
            img_label = tk.Label(img_frame, image=photo, bg='white')
            img_label.image = photo  # 参照を保持
            img_label.pack(padx=5, pady=5)
    
    # メッセージ用のフレーム
    msg_frame = tk.Frame(window, bg='#ffffff', relief='ridge', bd=2)
    msg_frame.pack(pady=10, padx=20, fill='x')
    
    # メッセージを表示
    msg_label = tk.Label(msg_frame, text=message, font=('Arial', 11), 
                        bg='#ffffff', fg='#333333',
                        wraplength=300, justify='center')
    msg_label.pack(pady=15, padx=10)
    
    # OKボタン
    def close_all():
        window.destroy()
        root.quit()  # mainloopを終了
    
    button_frame = tk.Frame(window, bg='#f0f8ff')
    button_frame.pack(pady=15)
    
    ok_button = tk.Button(button_frame, text="OK", command=close_all, 
                         font=('Arial', 12, 'bold'), width=8,
                         bg='#4169e1', fg='white', relief='raised', bd=3)
    ok_button.pack()
    
    # ウィンドウを中央に配置
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)
    y = (window.winfo_screenheight() // 2) - (window.winfo_height() // 2)
    window.geometry(f"+{x}+{y}")
    
    # Escキーでも閉じられるようにする
    window.bind('<Escape>', lambda e: close_all())
    window.focus_set()

def time_based_comment():
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    now = datetime.datetime.now()
    formatted_date = now.strftime('%-m月%-d日(%a) %-H時%-M分')
    
    # 時間帯に応じたメッセージと画像URLを設定
    if 4 <= now.hour < 5:
        message = "朝の4時よ！これから走りに出るんでしょ？"
        image_url = "https://github.com/user-attachments/assets/f0d529f5-a3a6-49dd-976f-ebbffd033933"
    elif 20 <= now.hour < 21:
        message = "じゃあ、おやすみっ！ ぐー。"
        image_url = "https://github.com/user-attachments/assets/ec4ca2b6-ecfd-4f31-bac0-7f65d528452f"
    elif 21 <= now.hour or now.hour < 4:
        message = "……すぅ……"
        image_url = "https://github.com/user-attachments/assets/764397db-ca26-4057-acac-3df4dc0091d0"
    elif now.weekday() == 6 and 12 <= now.hour < 13:
        message = "昼寝をするわっ！"
        image_url = "https://github.com/user-attachments/assets/e09e3022-e982-495e-ae35-7e6a4f77217d"
    else:
        message = "お姉ちゃんに任せなさいっ!"
        image_url = "https://github.com/user-attachments/assets/8c9dc9ce-58f7-4e1c-b5ae-f6027ef1cf4a"
    
    # カスタムアラートウィンドウを表示
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを隠す
    
    full_message = f"{formatted_date}\n(咲季): {message}"
    show_custom_alert(root, "咲季からのメッセージ", full_message, image_url)
    
    root.mainloop()  # イベントループを開始
    root.destroy()

def main():
    # スケジュールの設定
    schedule.every().day.at("04:00").do(time_based_comment)  # 朝4時
    schedule.every().day.at("20:00").do(time_based_comment)  # 夜8時
    schedule.every().day.at("21:00").do(time_based_comment)  # 夜9時
    schedule.every().sunday.at("12:00").do(time_based_comment)  # 日曜の昼12時
    
    print("咲季アラートシステムが開始されました...")
    print("終了するには Ctrl+C を押してください")
    
    # バックグラウンドでスケジュールを実行
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1分間隔でチェック

if __name__ == "__main__":
    main()