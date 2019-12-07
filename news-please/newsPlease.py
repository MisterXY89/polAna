
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


articles = NewsPlease.from_urls(urls)

print("Methoden & Attribute")
firstArticle = list(articles.values())[0]
print(f"{dir(firstArticle)}\n")

titles = []
for article in articles.items():
	ar = article[1]
	titles.append(ar.title)


# lexicon needed for sentiment analysis, needs to be downloaded once
# nltk.download('vader_lexicon')

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


articles2 = NewsPlease.from_urls(urls2)
for article in articles2.items():
	ar = article[1]
	print(ar.title)
	print(ar.authors)
	print(ar.language)