import datetime

def time_based_comment():
    now = datetime.datetime.now()
    if 4 <= now.hour < 5:
        print("朝の4時よ！これから走りに出るんでしょ？")
    elif 20 <= now.hour < 21:
        print("じゃあ、おやすみ！")
    elif now.weekday() == 6 and 12 <= now.hour < 13:
        print("昼寝をするわ！")
    else:
        print("testです！")

def main():
    time_based_comment()

if __name__ == "__main__":
    main()