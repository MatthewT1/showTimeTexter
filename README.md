# Showtime Texter 
##Description
This Python Script checks an RSS feed from Fandango for the showtimes of our local dollar theatre then looks up info for each movie through http://www.omdbapi.com, then it texts that info to a specified number through Gmail. I created a scheduled task to run this every Friday morning - this way my girlfriend and I don't miss any movies we've been waiting to see! 

##PreReqs
  * FeedParser
  * BeautifulSOup
  * YagMAil

You can easily install all of them through the 'stable-req.txt' file - just do:
* `pip install -r stable-req.txt`


You'll also need a Gmail account - I didn't feel like dealing with SMTP so I used YAG(https://github.com/kootenpv/yagmail) to handle it. 

##Usage
Change the first few lines to the info for your specific use case - these lines in particular will need to be updated:
```
global fandangoRSSURL = 'http://www.fandango.com/rss/moviesnearme_aarea_aagzu.rss'
global gmailAppPass = ''
global gmailUsername = 'insertEmailAddress@gmail.com'
global to = '@tomomail.net'
```
FandangoRSSURL can be generated at http://www.fandango.com/rss/moviefeed - just put in your zip code, tick off the theatre you want to monitor, then use the rss url for it in the variable.  

gmailAppPAss - this is an app specific password for gmail - see https://support.google.com/accounts/answer/185833?hl=en for more details. I use 2 factor authentication so I had to do this, if you don't you could use your normal gmail password. 

gmailUserNAme = the gmail address you're using to send out the text

to  - The person you want to text. Usually these are just phonenumber@carrier.com, see http://solutions.csueastbay.edu/questions.php?questionid=348 for more info. 

After changing those just do `python main.py` to test everything out - please submit a bug report if it doesn't work. 

To have it run automatically you can use Chron on Macs/*nix or Scheduled Tasks on Windows. 
