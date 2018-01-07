import urllib2
import BeautifulSoup as BS # BS short for beuatiful soup

csv_file = open("kontakte.csv", "w")

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
        gender = subsoup.ul.findAll("span", attrs={"data-gender": True })[0].string # wenn ich nicht weiss was element ist kann ich True schreiben
        email = subsoup.ul.findAll("span", attrs={"class": "email"})[0].string
        city = subsoup.ul.findAll("span", attrs={"data-city": True})[0].string
        print "email: {}, gender: {}, city: {}".format(email,gender,city) # in klammer am ende sind die dings von oben die in geschweifte eingesetzt werden
        csv_file.write("email: {}, gender: {}, city: {}".format(email,gender,city) + "\n")

csv_file.close()