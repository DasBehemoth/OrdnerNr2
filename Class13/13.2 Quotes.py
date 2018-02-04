import urllib2
import BeautifulSoup as BS
import random


if __name__=='__main__':
    url = 'http://quotes.yourdictionary.com/theme/marriage/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    quotes = soup.findAll(attrs={"class": "quoteContent"})

    slice = random.sample(quotes, 5)

    for x in slice:
        print x.text  # Urspruenglich damit probiert: soup.div.findAll(attrs={"class": "quoteContent"})[0].string bzw. .text hat aber alles nicht funktioniert, warum? Geht nur bei einem element, sonst ist es liste
