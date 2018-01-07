import urllib2
import BeautifulSoup as BS # BS short for beuatiful soup


if __name__=='__main__':
    url = 'https://en.wikipedia.org/wiki/Game_of_Thrones#Adaptation_schedule'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    #print soup.title.string # .string gibt nur text aus anders gibt es den ganzen code



    links = soup.table.findAll("a") # finde alle a in table
    rightlinks = soup.links.findAll
    for rightlinks in links:




    #for link in links:
       # subpage_link = url + link["href"] # alle links erkennen von der main page
      #  subresponse = urllib2.urlopen(subpage_link).read() # oeffne unterseite!
       # subsoup = BS.BeautifulSoup(subresponse) # mache soup aus subresponse!
        #viewers = subsoup.ul.findAll("h1")
        #print viewers