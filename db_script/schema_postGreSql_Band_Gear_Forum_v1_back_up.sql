CREATE TABLE Bidder
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidderName VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(25) DEFAULT NULL,
    admin BOOLEAN DEFAULT FALSE,
    email VARCHAR(80) DEFAULT NULL,
    secondary_email VARCHAR(80) DEFAULT NULL,
    userIcon_url VARCHAR(80) DEFAULT NULL,  -- Link to user's user's icon metadata file
    role_id INT NOT NULL,
    blocked BOOLEAN DEFAULT FALSE,

    FOREIGN KEY(role_id) REFERENCES ('role.id'),
    FOREIGN KEY(icon_url) REFERENCES ('metadata_file.id')
  );

CREATE TABLE Role
(
    id SERIAL NOT NULL PRIMARY KEY,
    Name VARCHAR(80) NOT NULL UNIQUE,
  );

CREATE TABLE BidGenre
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidGenre INT,
    bidder INT,
    bidGenreHeader VARCHAR(100) NOT NULL UNIQUE,

    FOREIGN KEY(bidder) REFERENCES Bidder(id)
  );

CREATE TABLE BidHeader
(
    id SERIAL NOT NULL PRIMARY KEY,
    initialBidder INT,
    bidGnre INT,
    bidHder VARCHAR(100) NOT NULL UNIQUE,
    numberOfBids INT NOT NULL,
    startedTime TIMESTAMP NOT NULL,

    FOREIGN KEY(initialBidder) REFERENCES Bidder(id),
    FOREIGN KEY(bidGnre) REFERENCES BidGenre(id)
  );

CREATE TABLE BidContent
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidderID INT,
    bidHead INT,
    bidderName VARCHAR(30) NOT NULL,
    bidContent VARCHAR(500) NOT NULL,
    editedTime TIMESTAMP NOT NULL,
    bundleImageI_url VARCHAR(80) DEFAULT NULL,  -- Link to bundle image metadata file
    bundleImageText TEXT,

    FOREIGN KEY(bidHead) REFERENCES BidHeader(id),
    FOREIGN KEY(imageID) REFERENCES ImageMetadata(imageID),
    FOREIGN KEY(bundleImageID) REFERENCES ImageMetadata(imageID)
  );

CREATE TABLE GearGroup
(
  id SERIAL NOT NULL PRIMARY KEY,
  gearGroup INT,
  bidderID INT,
  gearGroupHeader VARCHAR(100) NOT NULL UNIQUE,

  FOREIGN KEY(bidder) REFERENCES Bidder(id)
);

CREATE TABLE Gear
(
  id SERIAL NOT NULL PRIMARY KEY,
  gearCode INT,
  gearStatus INT,
  bidderID INT,
  bidHead INT,
  gearName VARCHAR(100) NOT NULL,
  gearDetails VARCHAR(500) NOT NULL,
  gearStory VARCHAR(500) NOT NULL,
  amountOffered INT NOT NULL,
  origPrice INT NOT NULL,
  comments VARCHAR(200) NOT NULL,
  editedTime TIMESTAMP NOT NULL,
  gearImageI_url VARCHAR(80) DEFAULT NULL,  -- Link to gear image metadata file
  gearImageText TEXT,

  FOREIGN KEY(bidderID) REFERENCES Bidder(id),
  FOREIGN KEY(bidHead) REFERENCES BidHeader(id)
  FOREIGN KEY(gearImageID) REFERENCES ImageMetadata(imageID),
);

CREATE TABLE BidExchange --This table will allow bidders to exchange equipment based on their bids.
(
    id SERIAL NOT NULL PRIMARY KEY,
    salesBidder INT NOT NULL, -- ID of the initial bidder (sales-bidder)
    purchaseBidder INT NOT NULL, -- ID of the bidder making the purchase offer
    equipmentOffer VARCHAR(100) NOT NULL, -- Description of the equipment offered
    equipmentRequested VARCHAR(100) NOT NULL, -- Description of the equipment requested
    agreedDeal BOOLEAN DEFAULT FALSE, -- Indicates if the deal is mutually agreed upon
    dealTimestamp TIMESTAMP NOT NULL, -- Timestamp when the deal was made

    FOREIGN KEY(salesBidder) REFERENCES Bidder(id),
    FOREIGN KEY(purchaseBidder) REFERENCES Bidder(id)
);

CREATE TABLE ImageMetadata
(
    imageID SERIAL NOT NULL PRIMARY KEY,
    imageLink TEXT NOT NULL,
    size VARCHAR(10) NOT NULL,
    resolution VARCHAR(20) NOT NULL
);

CREATE VIEW BidGenreList AS
SELECT bg.id, bg.bidGenreHeader, COUNT(bc.id) as count, MAX(bc.editedTime) AS latest
FROM BidGenre bg
LEFT JOIN BidHeader bhr ON (bg.id = bhr.bidGnre)
LEFT JOIN BidContent bc ON (bhr.id = bc.bidHead)
GROUP by bg.id, bg.bidGenreHeader;

CREATE VIEW BidList AS
SELECT bh.id, bh.initialBidder, bh.bidGnre, bh.bidHder,
COUNT(*) AS count, MIN(bc.editedTime) AS edited,
MAX(bc.editedTime) AS latest
FROM BidHeader bh
LEFT JOIN BidContent bc ON (bh.id = bc.bidHead)
GROUP BY bh.id, bh.bidHder, bh.initialBidder, bh.bidGnre
ORDER BY MAX(bc.editedTime) DESC;
