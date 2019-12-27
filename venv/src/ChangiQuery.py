import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import logging


log = logging.getLogger("logger")
URL = 'http://www.changiairport.com/en/flights/'
HEADERS = {'User-Agent': 'Mozilla/5'}


class ChangiQuery(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, arrdep, search=None, date=None, terminal=None, timing=None):
        """Return a Changi object with search, date, terminal, timing."""

        self.arrdep = arrdep
        if search is None:
            search = ''
        self.search = search
        if date is None:
            date = ''
        self.date = date
        if terminal is None:
            terminal = 'all'
        self.terminal = terminal
        if timing is None:
            timing = ''
        self.timing = timing

        log.info('Changi object initiated')

    @staticmethod
    def get_results(response):

        """Returns an organized json containing results"""

        result_table = response.findAll("div", {"class": "row flight-detail"})

        flight_status = []  # div- flight-status
        estimated_time = []  # span estimated-time
        times = []
        flight_code = []  # span- code
        airline = []  # span highlight
        #    terminal = [] #div- terminal
        #    belt = [] #div terminal-detail

        out = []

        for _ in range(len(result_table)):

            out_row = {}
            # print(result_table[_])

            flight_status_text = result_table[_].find('div', {"class": "flight-status"}).findChildren('span',recursive=False)
            # flight_status.append(flight_status_text[_].get_text())
            out_row['flight_status'] = flight_status_text[0].get_text()

            est_time_text = result_table[_].find('span', {"class": "estimated-time"})
            # estimated_time.append(est_time_text.get_text())
            out_row['estimated_time'] = est_time_text.get_text()

            times_text = result_table[_].find('span', {"class": "color-custom-1"})
            # times.append(times_text.get_text())
            out_row['times'] = times_text.get_text()

            flight_info = result_table[_].find('div', {"class": "flight-info"}).findChildren('span', recursive=False)

            # flight_code.append(flight_info[_].get_text())
            # airline.append(flight_info[_ + 1].get_text())
            out_row['flight_code'] = flight_info[0].get_text()
            out_row['airline'] = flight_info[1].get_text()
            out.append(out_row)

        return out

    def search_api(self):
        """Return the scrape results."""

        arrdep = self.arrdep
        search = self.search
        date = self.date
        terminal = self.terminal
        timing = self.timing

        log.info(
            'SEARCHING \n arrdep: {}, search: {}, date = {}, terminal = {}, timing = {}'.format(arrdep, search, date,
                                                                                                terminal,
                                                                                                timing))
        if search != '':
            search_term = '&searchTerm=' + search
        if date != '':
            date_term = '&date=' + date

        terminal_term = '&terminal=' + terminal
        time_term = "&time=all"

        search_url = '{}{}.html#?status={}{}{}{}{}'.format(URL, arrdep, arrdep, date_term, search_term,
                                                           terminal_term, time_term)
        driver = webdriver.Chrome()
        driver.get(search_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        log.info(search_url)

        out = self.get_results(soup)

        return out


# changi = ChangiQuery('arrivals', search='scoot', date='today')
# out = changi.search_api()
#
# print(out)






