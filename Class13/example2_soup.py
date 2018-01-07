import urllib2
import BeautifulSoup as BS # BS short for beuatiful soup


if __name__=='__main__':
    url = 'https://scrapebook22.appspot.com/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    # print soup.title.string # .string gibt nur text aus anders gibt es den ganzen code

    links = soup.table.findAll("a") # finde alle a in table
    for link in links:
        subpage_link = url + link["href"] # alle links erkennen von der main page
        subresponse = urllib2.urlopen(subpage_link).read() # oeffne unterseite!
        subsoup = BS.BeautifulSoup(subresponse) # mache soup aus subresponse!
        print subsoup.findAll("h1")#[1].string # suche sachen raus: von den H1 tags nimmt er das zweite [1]



