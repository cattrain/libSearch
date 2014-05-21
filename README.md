libSearch
=========

A tool for searching Library catalogs.

requires feedparser

To use, edit libSearch.py. edit:
d = feedparser.parse('http://nypl.bibliocommons.com/search/rss?commit=Search&display_quantity=5&formats=MUSIC_CD&q=' + e + '&searchOpt=catalogue&search_category=keyword&t=keyword')
replace the part in the brackets with your library search rss feed url, replacing the search query with ' + e + '

