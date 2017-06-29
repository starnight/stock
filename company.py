#!/bin/env python3

import urllib.request

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

    def getBreifCompanies(self):
        feildNames = ["公司代號", "公司名稱", "產業別", "營利事業統一編號"]
        breif = []

        indices = [self.getFeilds().index(fn) for fn in feildNames]

        for comp in self.getCompanies():
            breif.append([comp[idx] for idx in indices])

        return breif


if __name__ == '__main__':
    complist = CompanyList()
    complist.buildCompList()
    comps = complist.getBreifCompanies()
    for comp in comps:
        print(comp)
