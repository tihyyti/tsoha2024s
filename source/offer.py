import Productgroup
import Bidder

from datetime import datetime

class Offer:
    def __init__(self, id, bidder, productgroup, header):
        self.id = id
        self.bidder = bidder
        self.productgroup = productgroup
        self.header = header
        self.offercount = 0
        self.offerdate = datetime.now()
        self.lastoffer = None

    def Negotiation(self, bidder, productgroup, header):
        self.id = None
        self.bidder = bidder
        self.productgroup = productgroup
        self.header = header
        self.offercount = 0
        self.offerdate = datetime.now()
        self.lastoffer = None

    def Negotiationsummary(self, id, bidder, productgroup, header, offercount, offerdate, lastoffer):
        self.id = id
        self.bidder = bidder
        self.productgroup = productgroup
        self.header = header
        self.offercount = offercount
        self.offerdate = offerdate
        self.lastoffer = lastoffer

    # Getter methods
    def getId(self):
        return self.id

    def getBidder(self):
        return self.bidder

    def getProductgroup(self):
        return self.productgroup

    def getHeader(self):
        return self.header

    def getofferdate(self):
        return self.offerdate

    def getOffercount(self):
        return self.offercount

    def getLastoffer(self):
        return self.lastoffer

    # Setter methods
    def setId(self, id):
        self.id = id

    def setBidder(self, bidder):
        self.bidder = bidder

    def setProductgroup(self, productgroup):
        self.productgroup = productgroup

    def setHeader(self, header):
        self.header = header

    def setOfferdate(self, offerdate):
        self.offerdate = offerdate

    def setOffercount(self, offercount):
        self.offercount = offercount

    def setLastoffer(self, lastoffer):
        self.lastoffer = lastoffer
