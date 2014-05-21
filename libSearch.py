
e = raw_input()
f = open('test.log', 'w')
import feedparser
d = feedparser.parse('http://nypl.bibliocommons.com/search/rss?commit=Search&display_quantity=5&formats=MUSIC_CD&q=' + e + '&searchOpt=catalogue&search_category=keyword&t=keyword')
print d.feed.title

for post in d.entries:
	f.write(post.title)
	f.write('\n')
f.close()
