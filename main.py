import feedparser
from bs4 import BeautifulSoup
import urllib
import requests
import yagmail

#Variables
global fandangoRSSURL = 'http://www.fandango.com/rss/moviesnearme_aarea_aagzu.rss'
global gmailAppPass = ''
global gmailUsername = 'insertEmailAddress@gmail.com'
global to = '@tomomail.net'

def getMovies(rssURL):   
	#Grab the RSS feed and turn it into a Dict
	d = feedparser.parse(rssURL)
	#Use BEautifulSOup to parse the html from the RSS feed
	soup = BeautifulSoup(d['entries'][0]['summary_detail']['value'])
	movies = soup.find_all('a')
	#Go through that list and clean it up a bit
	movieNames = []
	for movie in movies:
		if(movie.get_text() != 'Search other theaters' ):
			movieNames.append(movie.get_text())
	#Return just the names as a list. 	
	return movieNames

def getMovieInfo(movieTitle):
	imdbJson = 'http://www.omdbapi.com/?t=%s&y=&plot=short&r=json' % (urllib.parse.quote(movieTitle))
	#Use Requests to pull the page and parse the JSON
	r = requests.get(imdbJson)
	infodDict = r.json()
	#return the Dict
	return infodDict


def main():
	yag = yagmail.SMTP(gmailUsername, gmailAppPass)
	textMessage = '---Now Playing at Silver Cinema---\r'
	movieNames = getMovies(fandangoRSSURL)

	for movie in movieNames :
		movieInfo = getMovieInfo(movie)
		textMessage += '\r' + movie + '\r'
		textMessage += movieInfo['Genre'] + '\r'
		textMessage += ('Released on %s\r' % movieInfo['Released'])
		textMessage += movieInfo['Awards'] + '\r'
		textMessage += ('Metacritic Score: %s/100\r' % movieInfo['Metascore'])
		textMessage += ('IMDB Rating: %s/10\r' % movieInfo['imdbRating'])
		textMessage += ('http://www.imdb.com/title/%s\r' % movieInfo['imdbID'])
		textMessage += '~~~~~~~~~~~~~~'
	yag.send(to, '~<3Silver Cinema is Now Showing<3~', textMessage)

main()
