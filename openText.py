import nltk
from nltk import pos_tag
from nltk.probability import FreqDist
from newspaper import Article, fulltext
import requests
import string
# dosya okuma ve kelimelere ayırma
f = open("text.txt", "r", encoding='utf8')
raw = f.read()
metin = raw
# Cümlelere bölüyor
cml = nltk.sent_tokenize(metin)
print(cml)
# metnin içindeki , leri .ları @ gibi işaretleri çıkarır sadece string ve sayıları gibi ifadeleri alır
temizMetin = metin.translate(str.maketrans('', '', string.punctuation))
# kelimelere bölüyor
genelKelimeler = nltk.word_tokenize(temizMetin)

fd = nltk.FreqDist(genelKelimeler)
# en çok kulanılan 5 kelimleyi alıyor
print(fd.most_common(5))
print('------------------------------------------')

taggent_sent = pos_tag(genelKelimeler)
print(taggent_sent)

f = open("textWrite.txt", "w", encoding='utf-8')


for element in taggent_sent:
    f.write(str(element) + "\n")

f.close()
