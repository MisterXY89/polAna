
import mediacloud.api

API_KEY = "69607f50090e4953805652c6e7591e9b21e02a7c2b4e58503d4ec44e3b2d26cc"
DOCS = "https://github.com/berkmancenter/mediacloud/blob/master/doc/api_2_0_spec/api_2_0_spec.md"

mc = mediacloud.api.MediaCloud(API_KEY)
res1 = mc.storyCount('impeachment AND president AND tags_id_media:58722749', 'publish_date:[NOW-1YEAR TO NOW]')
res2 = mc.storyCount('zimbabwe AND president AND tags_id_media:58722749', 'publish_date:[NOW-1YEAR TO NOW]')

print(res1['count']) # prints the number of stories found
print(res2['count']) # prints the number of stories found