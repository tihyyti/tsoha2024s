class Bidder:
    def __init__(self, bidderID, id):
        self.bidderaID = bidderID
        self.id = id

    def getId(self):
        return self.id

    def getBidderID(self):
        return self.bidderID
