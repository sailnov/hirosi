from datetime import datetime
import webbrowser, time
class AbeHirosi:
    def __init__(self):
        year = datetime.now().year + 1
        self.open_time = datetime(year, 1, 1, 0, 0, 0)
        self.url = "http://abehiroshi.la.coocan.jp/"
    def loop(self):
        print(self.open_time,"になったら",self.url,"を開きます。")
        while True:
            now = datetime.now().replace(microsecond=0)
            print('現在時刻：', now)
            if now == self.open_time:
                print('--------------------')
                print('指定の時間になったのでブラウザを開きます')
                print('--------------------')
                start = datetime.now()
                print('開始時刻：', start)
                webbrowser.open(self.url)
                end = datetime.now()
                print('終了時刻：', end)
                print('誤差：', end - start)
                break
            else:
                time.sleep(1)

if "__main__" == __name__:
    abe = AbeHirosi()
    abe.loop()