import bidder
from datetime import datetime

class Negotiation:
    def __init__(self, bidderID=-1, bidder="Bidder", negotiation=-1, offertext="Offertext"):
        self.offerID = -1
        self.bidderID = bidderID
        self.bidder = bidder
        self.negotiation = negotiation
        self.offerdate = datetime.now()
        self.offertext = offertext

    def setOfferID(self, offerID):
        self.offerID = offerID

    def getBidderID(self):
        return self.bidderID

    def getNegotiation(self):
        return self.negotiation

    def getBidder(self):
        return self.bidder

    def getOfferdate(self):
        return self.offerdate

    def getOffertext(self):
        return self.offertext