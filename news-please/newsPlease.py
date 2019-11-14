
# nltk general: https://www.nltk.org/book/
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from newsplease import NewsPlease

# PART 1
# show potential use-case of news-please

urls = [
	"https://www.nytimes.com/2019/11/05/us/politics/impeachment-trump.html",
	"https://www.breitbart.com/clips/2019/11/05/espaillat-sondlands-revised-testimony-is-a-smoking-gun/"
	]


titles = []
for url in urls:
	article = NewsPlease.from_url(url)
	titles.append(article.title)


# lexicon needed for sentiment analysis, needs to be downloaded once
nltk.download('vader_lexicon')

# https://opensourceforu.com/2016/12/analysing-sentiments-nltk/
sid = SentimentIntensityAnalyzer()
for sentence in titles:
	print(sentence)
	ss = sid.polarity_scores(sentence)
	for k in ss:
		print('{0}: {1}, '.format(k, ss[k]), end='')
	print()


# PART 2 
# show disadvantages of news-please
print("\n" + 70*"#")

urls2 = [
	"https://www.politico.eu/article/twitter-dropping-all-political-ads/",
	"https://www.sueddeutsche.de/politik/spd-walter-borjans-parteivorsitz-kanzlerkandidatur-1.4670436",
	"https://www.politico.eu/interactive/gun-violence-gun-crime-a-very-american-epidemic-las-vegas-columbine-sandy-hook-parkland-2020-presidential-campaign/",
	"https://www.zeit.de/kultur/2019-11/meinungsfreiheit-rechtsextremismus-afd-medien-verantwortung"
	]

for url in urls2:
	article = NewsPlease.from_url(url)
	print(article.title)
	print(article.authors)
	print(article.language)