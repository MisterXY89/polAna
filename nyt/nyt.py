#!/usr/bin/env python
from setup import *

api = ApiSetup()
app = AppSetup()

# for this small example this class is not necessarily needed
class NYT():
	def __init__(self,api,app):
		self.api = api
		self.app = app

	def getTopTitles(self):
		for entry in self.api.read(self.api.top_url):
			print(entry.title)

	def getTopShared(self, period):
		shared_url = api.build_shared_with_period(period)
		if not shared_url: 
			print(f"Error building URL for period {period}")
			return 
		for entry in api.read(shared_url):
			print(f"{entry.share_count}: {entry.title}")



nyt = NYT(api, app)
nyt.getTopTitles()
nyt.getTopShared(period=30)


