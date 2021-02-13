from os.path import exists

import bs4 as bs
import urllib.request

source = urllib.request.urlopen(
    'https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020LE.html').read()
soup = bs.BeautifulSoup(source, 'lxml')

table = soup.table

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]

    if "LECT\xa0" in row:
        print(row)
