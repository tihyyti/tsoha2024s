--PostgreSQL 16 schema:
--Data Types and Constraints:
--Use TEXT instead of VARCHAR for columns where the length is not strictly limited.
--Ensure password column in Bidder table is hashed for security.

--Indexes:
--Add indexes to frequently queried columns to improve performance.
--Foreign Key Constraints:
--Ensure all foreign key constraints are correctly defined.
--Timestamp Defaults:
--Set default values for timestamp columns to the current time.

CREATE TABLE Bidder (
    id SERIAL PRIMARY KEY,
    bidderName VARCHAR(30) NOT NULL UNIQUE,
    password TEXT DEFAULT NULL,
    admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE BidGenre (
    id SERIAL PRIMARY KEY,
    bidGenre INT,
    bidder INT,
    bidGenreHeader VARCHAR(100) NOT NULL UNIQUE,
    FOREIGN KEY (bidder) REFERENCES Bidder(id)
);

CREATE TABLE BidHeader (
    id SERIAL PRIMARY KEY,
    initialBidder INT,
    bidGnre INT,
    bidHder VARCHAR(100) NOT NULL UNIQUE,
    numberOfBids INT NOT NULL,
    startedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initialBidder) REFERENCES Bidder(id),
    FOREIGN KEY (bidGnre) REFERENCES BidGenre(id)
);

CREATE TABLE BidContent (
    id SERIAL PRIMARY KEY,
    bidderID INT,
    bidHead INT,
    bidderName VARCHAR(30) NOT NULL,
    bidContent TEXT NOT NULL,
    editedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bidHead) REFERENCES BidHeader(id)
);

CREATE TABLE GearGroup (
    id SERIAL PRIMARY KEY,
    gearGroup INT,
    bidderID INT,
    gearGroupHeader VARCHAR(100) NOT NULL UNIQUE,
    FOREIGN KEY (bidderID) REFERENCES Bidder(id)
);

CREATE TABLE Gear (
    id SERIAL PRIMARY KEY,
    gearCode INT,
    gearStatus INT,
    bidderID INT,
    bidHead INT,
    gearName VARCHAR(100) NOT NULL,
    gearDetails TEXT NOT NULL,
    gearStory TEXT NOT NULL,
    amountOffered INT NOT NULL,
    origPrice INT NOT NULL,
    comments TEXT NOT NULL,
    editedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bidderID) REFERENCES Bidder(id),
    FOREIGN KEY (bidHead) REFERENCES BidHeader(id)
);

CREATE TABLE BidExchange (
    id SERIAL PRIMARY KEY,
    salesBidder INT NOT NULL,
    purchaseBidder INT NOT NULL,
    equipmentOffer VARCHAR(100) NOT NULL,
    equipmentRequested VARCHAR(100) NOT NULL,
    agreedDeal BOOLEAN DEFAULT FALSE,
    dealTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (salesBidder) REFERENCES Bidder(id),
    FOREIGN KEY (purchaseBidder) REFERENCES Bidder(id)
);

CREATE VIEW BidGenreList AS
SELECT bg.id, bg.bidGenreHeader, COUNT(bc.id) AS count, MAX(bc.editedTime) AS latest
FROM BidGenre bg
LEFT JOIN BidHeader bhr ON (bg.id = bhr.bidGnre)
LEFT JOIN BidContent bc ON (bhr.id = bc.bidHead)
GROUP BY bg.id, bg.bidGenreHeader;

CREATE VIEW BidList AS
SELECT bh.id, bh.initialBidder, bh.bidGnre, bh.bidHder,
COUNT(*) AS count, MIN(bc.editedTime) AS edited,
MAX(bc.editedTime) AS latest
FROM BidHeader bh
LEFT JOIN BidContent bc ON (bh.id = bc.bidHead)
GROUP BY bh.id, bh.bidHder, bh.initialBidder, bh.bidGnre
ORDER BY MAX(bc.editedTime) DESC;

-- Indexes for performance
CREATE INDEX idx_bidder_name ON Bidder(bidderName);
CREATE INDEX idx_bid_genre_header ON BidGenre(bidGenreHeader);
CREATE INDEX idx_bid_header ON BidHeader(bidHder);
CREATE INDEX idx_bid_content ON BidContent(bidContent);
CREATE INDEX idx_gear_name ON Gear(gearName);