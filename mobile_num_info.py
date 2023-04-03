import mechanize
from bs4 import BeautifulSoup

def mobile_trace():
    url = "https://www.findandtrace.com/trace-mobile-number-location"

    brow = mechanize.Browser()
    brow.set_handle_robots(False)
    brow.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



    brow.open(url)
    brow.select_form(name="trace")
    brow['mobilenumber'] = str(input("Enter the Number : "))

    result = brow.submit()


    soup = BeautifulSoup(result.read(),'html.parser')

    table_extr = soup.find_all('table',class_="shop_table")
    print(len(table_extr))

    data_extra = table_extr[1].find('tfoot')
    data_extra = str(data_extra)
    data_extra = data_extra.replace("<tr>","")
    data_extra = data_extra.replace("</tr>","")
    data_extra = data_extra.replace("<th>","")
    data_extra = data_extra.replace("<td>","")
    data_extra = data_extra.replace("</td>","")
    data_extra = data_extra.replace("<tfoot>","")

    print(data_extra)

