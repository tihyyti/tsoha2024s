 Insert records into the BidExchange table:
Create the BidExchange table: First, make sure you have already created the BidExchange table with the specified columns:

CREATE TABLE BidExchange
(
    id SERIAL NOT NULL PRIMARY KEY,
    salesBidder INT NOT NULL,
    purchaseBidder INT NOT NULL,
    equipmentOffer VARCHAR(100) NOT NULL,
    equipmentRequested VARCHAR(100) NOT NULL,
    agreedDeal BOOLEAN DEFAULT FALSE,
    dealTimestamp TIMESTAMP NOT NULL
);

-- Add foreign key for purchaseBidder
ALTER TABLE Bidder
ADD CONSTRAINT fk_purchaseBidder
FOREIGN KEY (id) REFERENCES BidExchange(purchaseBidder);

-- Add foreign key for salesBidder
ALTER TABLE Bidder
ADD CONSTRAINT fk_salesBidder
FOREIGN KEY (id) REFERENCES BidExchange(salesBidder);


--Insert sample data: Now let’s insert some example records into the BidExchange table:
--Modify the sample data: Feel free to adjust the bidder IDs, equipment descriptions, agreement status, and timestamps according to your specific use case.
--Remember to replace the sample data with your actual values. The dealTimestamp should be in the format 'YYYY-MM-DD HH:MM:SS'.


-- Inserting a sample exchange where bidder 1 (salesBidder) offers a guitar to bidder 2 (purchaseBidder)
INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (1, 2, 'Electric Guitar', 'Drum Set', TRUE, '2024-07-19 10:30:00');

-- Another exchange: bidder 3 (salesBidder) offers a keyboard to bidder 4 (purchaseBidder)
INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (3, 4, 'Keyboard', 'Bass Guitar', FALSE, '2024-07-19 11:15:00');--Bidder 5 (salesBidder) offers a saxophone to Bidder 6 (purchaseBidder):

INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (5, 6, 'Alto Saxophone', 'Trumpet', TRUE, '2024-07-19 12:00:00');

--Bidder 7 (salesBidder) offers a drum set to Bidder 8 (purchaseBidder):

INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (7, 8, 'Drum Set', 'Electric Guitar', FALSE, '2024-07-19 12:30:00');

--Bidder 9 (salesBidder) offers a violin to Bidder 10 (purchaseBidder):

INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (9, 10, 'Violin', 'Cello', TRUE, '2024-07-19 13:15:00');

--Bidder 11 (salesBidder) offers a keyboard to Bidder 12 (purchaseBidder):

INSERT INTO BidExchange (salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp)
VALUES (11, 12, 'Keyboard', 'Flute', FALSE, '2024-07-19 14:00:00');


postgresql.org
stackoverflow.com
mydbops.com
stackoverflow.com
mssqltips.com
oracle-base.com
