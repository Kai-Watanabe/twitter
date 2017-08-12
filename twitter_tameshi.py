#ライブラリ
import tweepy
import os
import time
import datetime
from datetime import datetime, timedelta




#取得キー
CONSUMER_KEY='65OzS4TIhdjwxx9zDQFSUcls8'
CONSUMER_SECRET='WTISvUkBWum1AT5oBUdeq8voGWF2vvr9aymIFt3U7OpyYRfhtw'
ACCESS_TOKEN='867582419880165377-dGNug1G0kIqdZcKy8RAeTAjDBvAIAYQ'
ACCESS_SECRET='88YVCdg5lG5yARlLMRfnYGRNYDxy0BtPAFBt8sLEQkHxd'

auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#エラーの受け渡し
#class myException(Exception): pass

#Streaming APIで取得したツイートを処理するためのクラス
class MyStreamListener(tweepy.StreamListener):

    #ツイートを受信したときに呼び出されるメソッド
    #引数はツイートを表すstatusオブジェクト
    def on_status(self, status):
        today=datetime.now()
        print(today)
        todaystr=today.strftime('%m%d')
        tweet=status.text
        print(tweet)
        f=open('twitter_tameshi.text', 'a')
        f.write(todaystr)
        f.write(tweet)
        f.write('\n')
        f.close()



    def on_error(self, status_code):
        if status_code==420:
            return False

#twitterからpythonにメッセージを受信したときに、cp932でエラーがおこる
#認証情報をStreamListenerを指定してStreamオブジェクトを取得する
while True:
    try:
         stream=tweepy.Stream(auth, MyStreamListener())
         #フィルターをしたものを返す
         stream.filter(locations=[139.37,35.24,139.08,35.31],track=["犯罪","不審者","戸締り","つきまとわれる","防犯","わいせつ","公然わいせつ",
         "ちかん","痴漢","危険","声かけ","追いかけられる","脅迫","暴行",
         "凶悪","事件","詐欺","オレオレ","警察","ひったくり","侵入","万引き",
         "空き巣","犯人","泥棒","放浪","違反","違反","逃走","犯","嫌","嫌だ","いや","難しい","じゃまくさい","邪魔","忙し",
         "出来ない","こまった","疲れた","つかれた","こまる","つら","ムカつく","やば","許さない","くるし",
         "つらい","むかつく","だるい","やばい","ゆるせない","苦し","つまらない","不幸",
         "ついてない","死ぬ","しぬ","うざ","積んだ","つんだ","行きたくない"])


    except UnicodeEncodeError:
         print("unicode")
         today=datetime.now()
         print(today)
         todaystr=today.strftime('%m%d')
         f=open('twitter_tameshi.text', 'a')
         f.write(todaystr)
         f.write("unicode")
         f.close()


    except Exception:
        #ツイートを得られなかった場合、１０秒待機して再度取得を行う
        time.sleep(5)
        stream=tweepy.Stream(auth, MyStreamListener())
        stream.filter(locations=[139.37,35.24,139.08,35.31],track=["犯罪","不審者","戸締り","つきまとわれる","防犯","わいせつ","公然わいせつ",
        "ちかん","痴漢","危険","声かけ","追いかけられる","脅迫","暴行",
        "凶悪","事件","詐欺","オレオレ","警察","ひったくり","侵入","万引き",
        "空き巣","犯人","泥棒","放浪","違反","違反","逃走","犯","かけられ"])




#print(status.created_at,'@' + status.user.screen_name, status.text)
