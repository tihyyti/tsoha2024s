
import Productgroup
from datetime import datetime

class ProductgroupListItem:
    def __init__(self, rownumber, pgroup, count, valid):
        self.rownumber = rownumber
        self.pgroup = pgroup
        self.count = count
        self.valid = valid

    def getName(self):
        return self.pgroup.getName()

    def getCount(self):
        return self.count

    def getProductgroupId(self):
        return self.pgroup.getId()

    def getValid(self):
        return self.valid

