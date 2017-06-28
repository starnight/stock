#!/bin/env python3

import urllib.request
import io

class CompanyList:
    _url = "http://dts.twse.com.tw/opendata/t187ap03_L.csv"

    def buildCompList(self):
        with urllib.request.urlopen(self._url) as response:
            body = response.read().decode('big5', errors='ignore')
            l = body.replace("\"", "").split(sep="\r\n")
            self._companies = [row.split(sep=',') for row in l]

    def getCompanies(self):
        return self._companies[2:-1]

    def getFeilds(self):
        return self._companies[1]

if __name__ == '__main__':
    complist = CompanyList()
    complist.buildCompList()
    comps = complist.getCompanies()
    for comp in comps:
        print(comp)
    print(complist.getFeilds())
