import requests

class DataGarageAPI():
    def __init__(self):
        self.datagarageHomePageURL = "http://www.datagarage.io"
        self.apiURL = ""
        self.filters = {'selector':'', 'sort':'', 'skip':'', 'limit':'', 'fields':''}

    def fetchAll(self, dataID, returnList = True):
        req = requests.get(self.datagarageHomePageURL + "/api/" +dataID)
        return req.json() if returnList else req.text

    def fetchCustom(self, dataID, form, returnList = True):
        res = requests.get(self.datagarageHomePageURL + "/api/" + dataID, params=form)
        return res.json() if returnList else req.text

    def setURL(self, URL):
        self.apiURL = URL

    def setDataID(self, dataID):
        self.apiURL = self.datagarageHomePageURL + "/api/"  + dataID

    def setSelector(self, condition):
        self.filters['selector'] = ''
        for item in condition[0]:
            self.filters['selector'] += str(item)

        for cond in condition[1:]:
            self.filters['selector'] += " AND "
            for item in cond:
                self.filters['selector'] += str(item)

    def setSort(self, field, acs = True):
        self.filters['sort'] = field + ":" + ("acs" if acs is True else "desc")

    def setFields(self, fields):
        self.filters['fields'] = fields[0]
        for f in fields[1:]:
            self.filters['fields'] += "," + f

    def setSkip(self, skipNum):
        self.filters['skip'] = str(skipNum)

    def setLimits(self, limitNum):
        self.filters['limit'] = str(limitNum)

    def getRawData(self, returnList = True):
        req = requests.get(self.apiURL)
        return req.json() if returnList else req.text

    def getFilteredData(self, returnList = True):
        req = requests.get(self.apiURL, params = self.filters)
        return req.json() if returnList else req.text

    def resetFilter(self):
        for f in self.filters:
            f = ''


if __name__ == '__main__':
    dgAPI = DataGarageAPI()

    #example 1
    dgAPI.setDataID("5365dee31bc6e9d9463a0057")

    dgAPI.setSelector([["鄉鎮市區", "=", "文山區"], ["土地區段位置或建物區門牌","=","/辛亥路/"], ["交易年月", ">=", 10300]])
    dgAPI.setSort('車位總價元', acs = True)
    dgAPI.setFields(['總價元'])
    dgAPI.setSkip(0)
    dgAPI.setLimits(7)

    print (dgAPI.getFilteredData(returnList = True))
    dgAPI.resetFilter()

    #example 2
    print (dgAPI.fetchAll("5365dee31bc6e9d9463a0057"))
    print (dgAPI.fetchCustom("5365dee31bc6e9d9463a0057", {"limit":"3"}))

