
from setup import ApiSetup
from newsapi import NewsApiClient

api = ApiSetup()

# Init
newsapi = NewsApiClient(api_key=api.key)

# /v2/top-headlines
# raises error ValueError: cannot mix country/category param with sources param.
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# top_headlines = newsapi.get_top_headlines(q='bitcoin', category='business', language='en')


# change from to earlier
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin', sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com', from_param='2019-10-12', to='2019-12-11', language='en', sort_by='relevancy',page=2)


# print(top_headlines)
print(all_articles)
# /v2/sources
sources = newsapi.get_sources()