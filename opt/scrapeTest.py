import requests
from bs4 import BeautifulSoup

response = requests.get('https://live-tennis.eu/en/wta-live-ranking')

print("ステータスコード：{0}".format(response.status_code))

# HTMLからデータを引き出す。content を渡した方が文字化けする可能性を減らせる
data = BeautifulSoup(response.content, 'lxml')

print('ページタイトル：{0}'.format(data.title.text))

data_lists = data.select("tbody > tr > td")

print("データの個数{0}".format(len(data_lists)))

for li in data_lists:
    print("li: ", li.string)


# data.title.text #タイトルタグの中身のみを出力する
# data.find_all('a') #すべての「a」タグを出力する
# data.find(id='id_name') #id属性「id_name」に一致するタグを出力する
# data.find(class_='class_name') # 特定のクラスを抽出 
# data.find(text='Google') #特定のワード「Google」に完全一致する文字列を出力する
# data.select('a > #id_name > .class_name') #aタグの子要素id_nameの子要素class_name
# data.select('a[href^="href_text"]') #href属性がhref_textのaタグを取得
