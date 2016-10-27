#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "pagesource.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        select = soup.find(id="AirportList")
        for option in select.children:
            if option.name=='option':
                if option["value"].find('All') == -1:
                    data.append(option["value"])

    return data


def test():
    data = extract_airports(html_page)
    #assert len(data) == 15
    #assert "ATL" in data
    #assert "ABR" in data

if __name__ == "__main__":
    test()
