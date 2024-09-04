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

    FOREIGN KEY(role_id) REFERENCES Role(id),
    FOREIGN KEY(userIcon_url) REFERENCES ImageMetadata(id)
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
    bundleImage_id INT,  -- Link to bundle image metadata file
    bundleSound_id INT, -- Links to bundle sound sample metadata file

    FOREIGN KEY(bidHead) REFERENCES BidHeader(id),
    FOREIGN KEY(bundleImage_id) REFERENCES ImageMetadata(id),
    FOREIGN KEY(bundleSound_id) REFERENCES SoundClipMetadata(id)
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
  gearImage_id VARCHAR(80) DEFAULT NULL,  -- Links to gear image metadata file
  soundClip_id INT, -- Links to gear sound sample metadata file

  FOREIGN KEY(bidderID) REFERENCES Bidder(id),
  FOREIGN KEY(bidHead) REFERENCES BidHeader(id),
  FOREIGN KEY(gearImage_id) REFERENCES ImageMetadata(id),
  FOREIGN KEY(soundClip_id) REFERENCES SoundClipMetadata(id)
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
    id SERIAL NOT NULL PRIMARY KEY,
    imageName VARCHAR(100) NOT NULL,
    A_size VARCHAR(10) NOT NULL,
    resolution VARCHAR(20) NOT NULL,
    image_url VARCHAR(255) NOT NULL -- Link to the actual image file
);

CREATE TABLE SoundClipMetadata
(
    id SERIAL NOT NULL PRIMARY KEY,
    clipName VARCHAR(100) NOT NULL,
    format VARCHAR(10) NOT NULL, -- e.g., '.wav', '.mp3', etc.
    quality VARCHAR(30) NOT NULL, -- e.g., '24-bit WAV', '196 kbps MP3', etc.
    clipLengthInSeconds FLOAT NOT NULL,
    isStereo BOOLEAN NOT NULL,
    sample_url VARCHAR(255) NOT NULL -- Link to the actual sound sample file
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
