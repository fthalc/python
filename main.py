import nltk
from nltk import pos_tag
from nltk.probability import FreqDist
from newspaper import Article, fulltext
import requests
import string
url = 'https://tr.lipsum.com/'
a = Article(url)
a.download()
a.parse()
metin = a.text
cml = nltk.sent_tokenize(metin)
# metnin içindeki , leri .ları @ gibi işaretleri çıkarır sadece string ifadeleri alır
temizMetin = metin.translate(str.maketrans('', '', string.punctuation))
# kelimelere bölüyor
genelKelimeler = nltk.word_tokenize(temizMetin)

fd = nltk.FreqDist(genelKelimeler)
# en çok kulanılan 10 kelimleyi alıyor
print(fd.most_common(5))
print('------------------------------------------')

taggent_sent = pos_tag(genelKelimeler)
print(taggent_sent)
