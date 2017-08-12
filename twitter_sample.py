#ライブラリ
import tweepy
import os
import time
import datetime

#取得キー
CONSUMER_KEY='65OzS4TIhdjwxx9zDQFSUcls8'
CONSUMER_SECRET='WTISvUkBWum1AT5oBUdeq8voGWF2vvr9aymIFt3U7OpyYRfhtw'
ACCESS_TOKEN='867582419880165377-dGNug1G0kIqdZcKy8RAeTAjDBvAIAYQ'
ACCESS_SECRET='88YVCdg5lG5yARlLMRfnYGRNYDxy0BtPAFBt8sLEQkHxd'

auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#Streaming APIで取得したツイートを処理するためのクラス
class MyStreamListener(tweepy.StreamListener):

    #ツイートを受信したときに呼び出されるメソッド
    #引数はツイートを表すstatusオブジェクト
    def on_status(self, status):

        tweet="{time},{tweet}".format(time=status.created_at, tweet=status.text)
        print(status.created_at,'@' + status.user.screen_name, status.text)

    def on_error(self, status_code):
        if status_code==420:
            return False

while True:
    try:
         stream=tweepy.Stream(auth, MyStreamListener())
         #フィルターをしたものを返す
         stream.filter(track=["oneokrock"])
    except UnicodeEncodeError:
         print("unicode")
         print("\n\n")



    except Exception:
        #ツイートを得られなかった場合、１０秒待機して再度取得を行う
        time.sleep(5)
        stream=tweepy.Stream(auth, MyStreamListener())
        stream.filter(track=["oneokrock"])


#locations=[139.37,35.24,139.08,35.31]
#公開しているツイートをサンプリングしたストリームを受信する
#キーワード引数languagesで、日本語のツイートのみに絞り出す
#南端の経度、西端の緯度、北端の経度、東端の緯度
