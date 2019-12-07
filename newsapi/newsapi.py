
from setup import ApiSetup

api = ApiSetup()

options = {
	"q": "trump impeachment", 
	"from": "2019-11-06"
	}

u = api.url_builder(api.buildEverythingUrl(options))
print(u)
res = api.read(u)
print(res.articles[0].source.name)
print(res.totalResults)