import datetime
import locale

def time_based_comment():
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    now = datetime.datetime.now()
    formatted_date = now.strftime('%-m月%-d日(%a) %-H時%-M分')
    print(formatted_date)
    print("(咲季): ", end="")
    if 4 <= now.hour < 5:
        print("朝の4時よ！これから走りに出るんでしょ？")
    elif 20 <= now.hour < 21:
        print("じゃあ、おやすみ！")
    elif now.weekday() == 6 and 12 <= now.hour < 13:
        print("昼寝をするわ！")
    else:
        print("お姉ちゃんに任せなさいっ!")
    print()

def main():
    time_based_comment()

if __name__ == "__main__":
    main()