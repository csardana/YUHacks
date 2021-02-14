from os.path import exists

import bs4 as bs
import urllib.request
links = ['https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020AP.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020ED.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020EU.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020FA.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020GL.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020GS.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020HH.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020LE.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020LW.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020SB.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/FW2020SC.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/SU2020UG.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/SU2020GS.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/SU2020LW.html','https://apps1.sis.yorku.ca/WebObjects/cdm.woa/Contents/WebServerResources/SU2020SB.html']

for link in links:
    source = urllib.request.urlopen(
        link).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    table = soup.table
    firstAndSecondYr=0
    thirdAndFourthYr=0

    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if "LECT\xa0" in row:
           x = row[1].split(" ")
           if int(x[0]) >= 1000 & int(x[0]) < 3000:
               firstAndSecondYr = firstAndSecondYr + 80
           if int(x[0]) >= 3000 & int(x[0]) < 5000:
               thirdAndFourthYr =  thirdAndFourthYr + 30

    totalStudents = firstAndSecondYr + thirdAndFourthYr
    print(firstAndSecondYr)
    print(thirdAndFourthYr)
    print(totalStudents)
    
totalStudents = firstAndSecondYr + thirdAndFourthYr
studentsDriving = 8100
studentsTakingBus= totalStudents - (1750) * 7 + 812 + studentsDriving
gasConsumptionDrivingBrampton = 10 * studentsDriving * 34
gasConsumptionDrivingSauga = 32.1 * 10 * studentsDriving
gasConsumptionDrivingScarborough =  33 * 10 * studentsDriving

