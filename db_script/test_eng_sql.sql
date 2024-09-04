-- Add foreign key for purchaseBidder
ALTER TABLE Bidder ALTER COLUMN fk_salesBidder;
ALTER TABLE Bidder ALTER COLUMN fk_purchaseBidder
	
ALTER TABLE Bidder ADD fk_salesBidder INT;
ALTER TABLE Bidder ADD fk_purchaseBidder INT;
ALTER TABLE Bidder ADD FOREIGN KEY(fk_salesBidder) REFERENCES BidExchange(salesBidder);

ALTER TABLE Bidder 
	FOREIGN KEY(fk_salesBidder) REFERENCES BidExchange(salesBidder);

TABLE Bidder FOREIGN KEY(fk_purchaseBidder) REFERENCES BidExchange(purchaseBidder);


